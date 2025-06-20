/***
 * FANCC DOCS
 */

console.log("%cFANCC DOCS", "color: blue;font-size: 20px;border: 1px solid black;padding:5px");
document.addEventListener("DOMContentLoaded", function(){
    document.querySelectorAll("a.reference.external").forEach(e=>{
        e.target = "_blank";
    });
});
