document.addEventListener("DOMContentLoaded", function() {
    fetch("data.json") 
        .then(response => response.json())
        .then(data => {
            const tableBody = document.getElementById("file-list");
            data.forEach(file => {
                let rowClass = file.type === "folder" ? "folder" : "";
                if (file.name.includes("hidden")) rowClass = "hidden-folder";

                let row = `<tr class="${rowClass}">
                    <td><a href="${file.path}">${file.name}</a></td>
                    <td>${file.size}</td>
                    <td>${file.date}</td>
                </tr>`;
                tableBody.innerHTML += row;
            });
        });
});

// Sorting function
function sortTable(columnIndex) {
    let table = document.getElementById("fileTable");
    let rows = Array.from(table.rows).slice(1);
    let sortedRows = rows.sort((a, b) => 
        a.cells[columnIndex].innerText.localeCompare(b.cells[columnIndex].innerText)
    );
    table.tBodies[0].append(...sortedRows);
}