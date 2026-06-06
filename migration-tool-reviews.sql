-- ==========================================
-- GlobalTradeHub: Tool Reviews + Subscribers
-- Migration Date: 2026-06-06
-- ==========================================

-- 1. Tool Reviews Table
CREATE TABLE IF NOT EXISTS tool_reviews (
  id         BIGSERIAL PRIMARY KEY,
  tool_id    VARCHAR(50) NOT NULL,
  user_id    UUID REFERENCES auth.users(id) NOT NULL,
  rating     SMALLINT NOT NULL CHECK (rating >= 1 AND rating <= 5),
  content    TEXT DEFAULT '',
  created_at TIMESTAMPTZ DEFAULT NOW(),
  updated_at TIMESTAMPTZ DEFAULT NOW(),
  -- Each user can only review each tool once
  UNIQUE(tool_id, user_id)
);

-- 2. Subscribers Table
CREATE TABLE IF NOT EXISTS subscribers (
  id           BIGSERIAL PRIMARY KEY,
  email        VARCHAR(255) NOT NULL UNIQUE,
  language     VARCHAR(10) DEFAULT 'zh',
  source       VARCHAR(50) DEFAULT 'hero',
  status       VARCHAR(20) DEFAULT 'active' CHECK (status IN ('active','unsubscribed','bounced')),
  subscribed_at TIMESTAMPTZ DEFAULT NOW(),
  unsubscribed_at TIMESTAMPTZ
);

-- 3. RLS Policies for tool_reviews
ALTER TABLE tool_reviews ENABLE ROW LEVEL SECURITY;

-- Anyone can read reviews
CREATE POLICY "Anyone can read tool reviews" ON tool_reviews
  FOR SELECT USING (true);

-- Only authenticated users can insert (their own)
CREATE POLICY "Authenticated users can review tools" ON tool_reviews
  FOR INSERT WITH CHECK (auth.role() = 'authenticated' AND auth.uid() = user_id);

-- Users can update their own reviews
CREATE POLICY "Users can update own reviews" ON tool_reviews
  FOR UPDATE USING (auth.uid() = user_id);

-- Users can delete their own reviews
CREATE POLICY "Users can delete own reviews" ON tool_reviews
  FOR DELETE USING (auth.uid() = user_id);

-- 4. RLS Policies for subscribers
ALTER TABLE subscribers ENABLE ROW LEVEL SECURITY;

-- Anyone can subscribe (insert)
CREATE POLICY "Anyone can subscribe" ON subscribers
  FOR INSERT WITH CHECK (true);

-- Only authenticated admins can read subscribers (you'll manage this manually)
CREATE POLICY "Only service role can read subscribers" ON subscribers
  FOR SELECT USING (false);

-- 5. Indexes for performance
CREATE INDEX IF NOT EXISTS idx_tool_reviews_tool_id ON tool_reviews(tool_id);
CREATE INDEX IF NOT EXISTS idx_tool_reviews_user_id ON tool_reviews(user_id);
CREATE INDEX IF NOT EXISTS idx_subscribers_email ON subscribers(email);
CREATE INDEX IF NOT EXISTS idx_subscribers_status ON subscribers(status);

-- 6. Grant permissions
GRANT SELECT, INSERT, UPDATE, DELETE ON tool_reviews TO authenticated, anon, service_role;
GRANT USAGE ON SEQUENCE tool_reviews_id_seq TO authenticated, anon, service_role;
GRANT SELECT, INSERT ON subscribers TO anon, authenticated, service_role;
GRANT USAGE ON SEQUENCE subscribers_id_seq TO anon, authenticated, service_role;
