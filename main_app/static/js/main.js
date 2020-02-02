sortTable();

function sortTable() {
    var table, rows, switching, i, x, y, shouldSwitch;
    table = document.getElementById("scoreBoard");
    switching = true;
    
    while (switching) {
      switching = false;
      rows = table.rows;

      for (i = 1; i < (rows.length - 1); i++) {
       
        shouldSwitch = false;
        
        x = rows[i].getElementsByTagName("TH")[1];
        y = rows[i + 1].getElementsByTagName("TH")[1];
       
        if (Number(y.innerHTML) > Number(x.innerHTML)) {
          shouldSwitch = true;
          break;
        }
      }
      if (shouldSwitch) {
        rows[i].parentNode.insertBefore(rows[i + 1], rows[i]);
        switching = true;
      }
    }
}