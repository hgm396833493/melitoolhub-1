import os

workspace = r'D:\workspace'
html_files = [f for f in os.listdir(workspace) if f.endswith('.html')]

# 移动端菜单切换JavaScript
mobile_menu_js = '''
<script>
// Mobile menu toggle
document.addEventListener('DOMContentLoaded', function() {
  const navToggle = document.getElementById('nav-toggle');
  const navLinks = document.getElementById('nav-links');
  
  if (navToggle && navLinks) {
    navToggle.addEventListener('click', function() {
      navLinks.classList.toggle('open');
    });
    
    // Close menu when clicking on a link
    navLinks.querySelectorAll('a').forEach(function(link) {
      link.addEventListener('click', function() {
        navLinks.classList.remove('open');
      });
    });
  }
});
</script>
'''

modified = 0
errors = 0

for fname in html_files:
    fpath = os.path.join(workspace, fname)
    try:
        with open(fpath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 检查是否已经有移动端菜单JS
        if 'nav-toggle' in content and 'classList.toggle' in content:
            print(f'Skipped (already has mobile menu JS): {fname}')
            continue
        
        # 在 </body> 前插入 JavaScript
        if '</body>' in content:
            content = content.replace('</body>', mobile_menu_js + '\n</body>')
            
            with open(fpath, 'w', encoding='utf-8') as f:
                f.write(content)
            modified += 1
            print(f'Modified: {fname}')
        else:
            print(f'Error: {fname} has no </body> tag')
            errors += 1
    except Exception as e:
        errors += 1
        print(f'Error {fname}: {e}')

print(f'\nDone! Modified: {modified}, Errors: {errors}')
