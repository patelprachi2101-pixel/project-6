import os

filepath = r'c:\Users\Laptop\OneDrive\Desktop\project-6\tenant-script.js'
with open(filepath, 'r', encoding='utf-8') as f:
    text = f.read()

target = """            card.innerHTML = `
                <div class="property-image" style="background-image: url('${mainImgSrc}');">
                    <span class="badge" style="background-color: var(--primary-color);">New</span>
                </div>
                <div class="property-details">
                    <div class="price">₹${Math.floor(Math.random() * 20 + 10)},000<span>/mo</span></div>
                    <h3>${prop.title || (prop.type ? prop.type.charAt(0).toUpperCase() + prop.type.slice(1) + ' for Rent' : 'Premium Property')}</h3>"""

replacement = """            const listingSuffix = (prop.listingType === 'sell' || prop.type === 'house') ? '' : '<span>/mo</span>';
            const defaultSuffix = (prop.listingType === 'sell' || prop.type === 'house') ? ' for Sale' : ' for Rent';
            
            card.innerHTML = `
                <div class="property-image" style="background-image: url('${mainImgSrc}');">
                    <span class="badge" style="background-color: var(--primary-color);">New</span>
                </div>
                <div class="property-details">
                    <div class="price">₹${prop.price ? Number(prop.price).toLocaleString('en-IN') : Math.floor(Math.random() * 20 + 10) + ',000'}${listingSuffix}</div>
                    <h3>${prop.title || (prop.type ? prop.type.charAt(0).toUpperCase() + prop.type.slice(1) + defaultSuffix : 'Premium Property')}</h3>"""

text = text.replace(target, replacement)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(text)
print('Done js replacement!')
