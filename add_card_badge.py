import os, re

def add_badge(file_path, badge_text, badge_color, badge_bg):
    if not os.path.exists(file_path): return
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # We want to replace:
    # <div class="price">...</div>
    # <h3>...</h3>
    # With:
    # <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.5rem;">
    #    <div class="price" style="margin-bottom: 0;">...</div>
    #    <span style="background-color: {badge_bg}; color: {badge_color}; padding: 0.2rem 0.6rem; border-radius: 4px; font-size: 0.75rem; font-weight: 600; text-transform: uppercase; white-space: nowrap;">{badge_text}</span>
    # </div>
    # <h3>...</h3>

    # Find all occurrences of <div class="price">...</div>
    pattern = r'(<div class="price">.*?</div>)(\s*<h3>.*?</h3>)'
    
    def replacer(match):
        price_div = match.group(1).replace('margin-bottom: 0.5rem;', '').replace('class="price"', 'class="price" style="margin-bottom: 0;"')
        h3_tag = match.group(2)
        
        # Check if already modified
        if 'justify-content: space-between' in price_div:
            return match.group(0)
            
        replacement = f'''<div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.5rem;">
                        {price_div}
                        <span style="background-color: {badge_bg}; color: {badge_color}; padding: 0.2rem 0.6rem; border-radius: 4px; font-size: 0.75rem; font-weight: 600; text-transform: uppercase; white-space: nowrap; height: fit-content;">{badge_text}</span>
                    </div>{h3_tag}'''
        return replacement

    new_content = re.sub(pattern, replacer, content)
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)

# Apply to static files
add_badge('generate_houses.js', 'For Sale', '#2ecc71', 'rgba(46, 204, 113, 0.2)')
add_badge('generate_pgs.js', 'For Rent', '#3498db', 'rgba(52, 152, 219, 0.2)')
add_badge('generate_villas.js', 'For Rent', '#3498db', 'rgba(52, 152, 219, 0.2)')
add_badge('generate_apartments.js', 'For Rent', '#3498db', 'rgba(52, 152, 219, 0.2)')
add_badge('tenant-home.html', 'For Rent', '#3498db', 'rgba(52, 152, 219, 0.2)')

# Modify tenant-script.js
js_file = 'tenant-script.js'
with open(js_file, 'r', encoding='utf-8') as f:
    js_content = f.read()

target_js = """                <div class="property-details">
                    <div class="price">₹${prop.price ? Number(prop.price).toLocaleString('en-IN') : Math.floor(Math.random() * 20 + 10) + ',000'}${listingSuffix}</div>
                    <h3>"""

replacement_js = """                <div class="property-details">
                    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.5rem;">
                        <div class="price" style="margin-bottom: 0;">₹${prop.price ? Number(prop.price).toLocaleString('en-IN') : Math.floor(Math.random() * 20 + 10) + ',000'}${listingSuffix}</div>
                        <span style="background-color: ${prop.listingType === 'sell' || prop.type === 'house' ? 'rgba(46, 204, 113, 0.2)' : 'rgba(52, 152, 219, 0.2)'}; color: ${prop.listingType === 'sell' || prop.type === 'house' ? '#2ecc71' : '#3498db'}; padding: 0.2rem 0.6rem; border-radius: 4px; font-size: 0.75rem; font-weight: 600; text-transform: uppercase; white-space: nowrap; height: fit-content;">${prop.listingType === 'sell' || prop.type === 'house' ? 'For Sale' : 'For Rent'}</span>
                    </div>
                    <h3>"""

if target_js in js_content:
    js_content = js_content.replace(target_js, replacement_js)
    with open(js_file, 'w', encoding='utf-8') as f:
        f.write(js_content)

print('Card badges updated successfully!')
