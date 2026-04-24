// Zdrowie.fit — strona "Artykuły": filtry + wyszukiwarka
(function () {
    'use strict';

    const grid = document.getElementById('articles-grid');
    const empty = document.getElementById('articles-empty');
    const searchInput = document.getElementById('articles-search');
    const filterBtns = document.querySelectorAll('.filter-btn');
    if (!grid) return;

    const cards = Array.from(grid.querySelectorAll('.article-card'));
    let activeCategory = 'all';
    let searchQuery = '';

    // Z URL-a: ?category=xxx&search=yyy
    const urlParams = new URLSearchParams(window.location.search);
    const urlCat = urlParams.get('category');
    const urlSearch = urlParams.get('search');
    if (urlCat) {
        activeCategory = urlCat;
        filterBtns.forEach(b => b.classList.toggle('active', b.dataset.category === urlCat));
    }
    if (urlSearch && searchInput) {
        searchInput.value = urlSearch;
        searchQuery = urlSearch.toLowerCase();
    }

    function slugFromCard(card) {
        const text = card.querySelector('.article-card__category')?.textContent.trim().toLowerCase() || '';
        return text.replace(/\s+/g, '-');
    }

    function apply() {
        let visible = 0;
        cards.forEach(card => {
            const title = card.querySelector('h3')?.textContent.toLowerCase() || '';
            const desc = card.querySelector('p')?.textContent.toLowerCase() || '';
            const catText = card.querySelector('.article-card__category')?.textContent.toLowerCase() || '';
            const matchesSearch = !searchQuery || title.includes(searchQuery) || desc.includes(searchQuery) || catText.includes(searchQuery);
            const matchesCat = activeCategory === 'all' || catText.includes(activeCategory.toLowerCase()) || slugFromCard(card).includes(activeCategory.toLowerCase());
            const show = matchesSearch && matchesCat;
            card.style.display = show ? '' : 'none';
            if (show) visible++;
        });
        if (empty) empty.hidden = visible > 0;
    }

    filterBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            filterBtns.forEach(b => b.classList.remove('active'));
            btn.classList.add('active');
            activeCategory = btn.dataset.category;
            apply();
        });
    });

    if (searchInput) {
        let t;
        searchInput.addEventListener('input', () => {
            clearTimeout(t);
            t = setTimeout(() => {
                searchQuery = searchInput.value.toLowerCase().trim();
                apply();
            }, 200);
        });
    }

    apply();
})();
