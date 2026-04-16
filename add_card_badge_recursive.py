import os, re

def add_badge(file_path):
    # Only for files that exist and are html or js
    if not os.path.exists(file_path): return
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # We want to replace:
    # <div class="price">...</div>
    # <h3>...</h3>
    
    # But wait, we need to know whether it's for rent or sale!
    # If the price has /mo, it's Rent. If not, Sale.
    # To be safe, if it's already modified, skip it.
    
    # We use a replacer function
    pattern = r'(<div class="price">[\s\S]*?</div>)(\s*<h3>[\s\S]*?</h3>)'
    
    modified = False
    
    def replacer(match):
        price_div = match.group(1).replace('margin-bottom: 0.5rem;', '').replace('class="price"', 'class="price" style="margin-bottom: 0;"')
        h3_tag = match.group(2)
        
        # Check if already modified
        if 'justify-content: space-between' in price_div:
            return match.group(0)
            
        badge_text = 'For Rent'
        badge_color = '#3498db'
        badge_bg = 'rgba(52, 152, 219, 0.2)'
        
        # Determine from contents of h3 or price
        if '/mo' not in price_div and 'Sale' in h3_tag:
            badge_text = 'For Sale'
            badge_color = '#2ecc71'
            badge_bg = 'rgba(46, 204, 113, 0.2)'
        elif 'house' in file_path.lower():
            # In generate_houses, we removed /mo, so they are all For Sale
            badge_text = 'For Sale'
            badge_color = '#2ecc71'
            badge_bg = 'rgba(46, 204, 113, 0.2)'
            
        nonlocal modified
        modified = True
        
        replacement = f'''<div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.5rem;">
                        {price_div}
                        <span style="background-color: {badge_bg}; color: {badge_color}; padding: 0.2rem 0.6rem; border-radius: 4px; font-size: 0.75rem; font-weight: 600; text-transform: uppercase; white-space: nowrap; height: fit-content;">{badge_text}</span>
                    </div>{h3_tag}'''
        return replacement

    new_content = re.sub(pattern, replacer, content)
    if modified:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)

# Apply to every html file in all subdirectories and current directory
for root, dirs, files in os.walk(r'c:\Users\Laptop\OneDrive\Desktop\project-6'):
    for file in files:
        if file.endswith('.html') or file.endswith('.js'):
            add_badge(os.path.join(root, file))

print('Card badges updated correctly everywhere!')
