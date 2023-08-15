let infoGrid = document.querySelectorAll('.post-preview-info-grid')
// grid info div as href
infoGrid.forEach(element =>{
    element.addEventListener('click', () => {
        const url = element.getElementsByTagName('a').item(0).getAttribute('href')
        location.href = url
    })
}, infoGrid)
