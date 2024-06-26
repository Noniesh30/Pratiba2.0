const sideMenu = document.querySelector("aside");
const profileBtn = document.querySelector("#profile-btn");
const themeToggler = document.querySelector(".theme-toggler");
const nextDay = document.getElementById('nextDay');
const prevDay = document.getElementById('prevDay');

profileBtn.onclick = function() {
    sideMenu.classList.toggle('active');
}
window.onscroll = () => {
    sideMenu.classList.remove('active');
    if(window.scrollY > 0){document.querySelector('header').classList.add('active');}
    else{document.querySelector('header').classList.remove('active');}
}

themeToggler.onclick = function() {
    document.body.classList.toggle('dark-theme');
    themeToggler.querySelector('span:nth-child(1)').classList.toggle('active')
    themeToggler.querySelector('span:nth-child(2)').classList.toggle('active')
}

document.addEventListener('DOMContentLoaded', function() {
    fetch('/api')
        .then(response => response.json())
        .then(data => {
            const tableBody = document.getElementById('exam-timetable').querySelector('tbody');
            data.forEach(item => {
                const row = document.createElement('tr');
                row.innerHTML = `
                    <td>${item.Subject}</td>
                    <td>${item.Score}</td>
                    <td>${item.Wrong}</td>
                    <td>${item.Attempted}</td>
                    <td>${item.Unattempted}</td>
                `;
                tableBody.insertBefore(row, tableBody.firstChild);
            });
        })
        .catch(error => console.error('Error fetching data:', error));
});