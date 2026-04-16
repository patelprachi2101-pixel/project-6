import os

html_files = [
    'generate_houses.js', 'generate_villas.js', 'generate_pgs.js', 'generate_apartments.js', 'tenant-home.html', 'tenant-my-properties.html'
]

target_html = """                    <h2 class="modal-title" id="modal-title">Property Title</h2>
                    <p class="modal-location" id="modal-loc">Property Location</p>
                    <div class="modal-amenities">"""

replacement_html = """                    <h2 class="modal-title" id="modal-title">Property Title</h2>
                    <p class="modal-location" id="modal-loc">Property Location</p>
                    <span id="modal-listing-type" style="display:inline-block; margin-top:0.5rem; padding:0.2rem 0.6rem; font-size:0.85rem; font-weight:600; border-radius:4px;">For Rent</span>
                    <div class="modal-amenities">"""

for f in html_files:
    if os.path.exists(f):
        with open(f, 'r', encoding='utf-8') as file:
            content = file.read()
        if target_html in content:
            content = content.replace(target_html, replacement_html)
            with open(f, 'w', encoding='utf-8') as file:
                file.write(content)

js_file = 'tenant-script.js'
with open(js_file, 'r', encoding='utf-8') as f:
    js_content = f.read()

target_js = """                document.getElementById('modal-title').textContent = title;
                document.getElementById('modal-loc').textContent = loc;
                if (url) {
                    document.getElementById('modal-main-img').src = url;
                }"""

replacement_js = """                document.getElementById('modal-title').textContent = title;
                document.getElementById('modal-loc').textContent = loc;
                if (url) {
                    document.getElementById('modal-main-img').src = url;
                }

                // Dynamically update modal listing type based on price display
                const priceText = card.querySelector('.price').textContent.toLowerCase();
                const listingTypeText = priceText.includes('/mo') ? 'For Rent' : 'For Sale';
                const modalListingType = document.getElementById('modal-listing-type');
                if (modalListingType) {
                    modalListingType.textContent = listingTypeText;
                    if (listingTypeText === 'For Sale') {
                        modalListingType.style.backgroundColor = 'rgba(46, 204, 113, 0.2)';
                        modalListingType.style.color = '#2ecc71';
                    } else {
                        modalListingType.style.backgroundColor = 'rgba(52, 152, 219, 0.2)';
                        modalListingType.style.color = '#3498db';
                    }
                }"""

if target_js in js_content:
    js_content = js_content.replace(target_js, replacement_js)
    with open(js_file, 'w', encoding='utf-8') as f:
        f.write(js_content)

print('Updating modal HTML/JS logic completed successfully!')
