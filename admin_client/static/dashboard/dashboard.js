window.onload = function () {
    hideTabsExceptId('#main-dashboard');
    showChart();
}

function selectDashboardTab(elem) {
    hideTabsExceptId(elem.dataset.bsToggle);
}

function hideTabsExceptId(id) {
    const collapsable_list = document.querySelectorAll('.multi-dashboard');
    collapsable_list.forEach(elem => {
        '#' + elem.id != id ? new bootstrap.Collapse(elem, {toggle: false}).hide() : new bootstrap.Collapse(elem, {toggle: false}).show();
    });
}