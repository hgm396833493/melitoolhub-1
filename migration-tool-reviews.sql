-- ==========================================
-- GlobalTradeHub: Tool Reviews + Subscribers
-- Migration Date: 2026-06-06
-- 直接复制到 Supabase SQL Editor 执行
-- ==========================================

-- 1. Subscribers Table (邮件订阅)
CREATE TABLE IF NOT EXISTS subscribers (
  id             BIGSERIAL PRIMARY KEY,
  email          VARCHAR(255) NOT NULL UNIQUE,
  language       VARCHAR(10) DEFAULT 'zh',
  source         VARCHAR(50) DEFAULT 'hero',
  status         VARCHAR(20) DEFAULT 'active' CHECK (status IN ('active','unsubscribed','bounced')),
  subscribed_at  TIMESTAMPTZ DEFAULT NOW(),
  unsubscribed_at TIMESTAMPTZ
);

-- 2. Tool Reviews Table (工具评价)
CREATE TABLE IF NOT EXISTS tool_reviews (
  id         BIGSERIAL PRIMARY KEY,
  tool_id    VARCHAR(50) NOT NULL,
  user_id    VARCHAR(100) NOT NULL,
  user_name  VARCHAR(100) DEFAULT 'Anonymous',
  rating     SMALLINT NOT NULL CHECK (rating >= 1 AND rating <= 5),
  content    TEXT DEFAULT '',
  created_at TIMESTAMPTZ DEFAULT NOW(),
  updated_at TIMESTAMPTZ DEFAULT NOW()
);

-- 每个用户每个工具只能评价一次（如果user_id相同）
CREATE UNIQUE INDEX IF NOT EXISTS idx_one_review_per_user
  ON tool_reviews(tool_id, user_id);

-- ==========================================
-- 3. RLS Policies
-- ==========================================

-- subscribers: 任何人可订阅
ALTER TABLE subscribers ENABLE ROW LEVEL SECURITY;
DROP POLICY IF EXISTS "Anyone can subscribe" ON subscribers;
CREATE POLICY "Anyone can subscribe" ON subscribers
  FOR INSERT WITH CHECK (true);

-- subscribers: 任何人可读取（用于检查重复）
DROP POLICY IF EXISTS "Anyone can read subscribers" ON subscribers;
CREATE POLICY "Anyone can read subscribers" ON subscribers
  FOR SELECT USING (true);

-- tool_reviews: 任何人可读
ALTER TABLE tool_reviews ENABLE ROW LEVEL SECURITY;
DROP POLICY IF EXISTS "Anyone can read tool reviews" ON tool_reviews;
CREATE POLICY "Anyone can read tool reviews" ON tool_reviews
  FOR SELECT USING (true);

-- tool_reviews: 任何人可提交评价
DROP POLICY IF EXISTS "Anyone can insert reviews" ON tool_reviews;
CREATE POLICY "Anyone can insert reviews" ON tool_reviews
  FOR INSERT WITH CHECK (true);

-- tool_reviews: 可更新自己的评价（通过user_id匹配）
DROP POLICY IF EXISTS "Users can update own reviews" ON tool_reviews;
CREATE POLICY "Users can update own reviews" ON tool_reviews
  FOR UPDATE USING (true);

-- tool_reviews: 可删除自己的评价
DROP POLICY IF EXISTS "Users can delete own reviews" ON tool_reviews;
CREATE POLICY "Users can delete own reviews" ON tool_reviews
  FOR DELETE USING (true);

-- ==========================================
-- 4. Indexes
-- ==========================================
CREATE INDEX IF NOT EXISTS idx_tool_reviews_tool_id ON tool_reviews(tool_id);
CREATE INDEX IF NOT EXISTS idx_subscribers_email ON subscribers(email);
CREATE INDEX IF NOT EXISTS idx_subscribers_status ON subscribers(status);

-- ==========================================
-- 5. Grant Permissions
-- ==========================================
GRANT SELECT, INSERT, UPDATE, DELETE ON tool_reviews TO anon, authenticated, service_role;
GRANT USAGE ON SEQUENCE tool_reviews_id_seq TO anon, authenticated, service_role;
GRANT SELECT, INSERT ON subscribers TO anon, authenticated, service_role;
GRANT USAGE ON SEQUENCE subscribers_id_seq TO anon, authenticated, service_role;
