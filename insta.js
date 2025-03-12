// all the requirements
let sidebar = document.querySelector(".sidebar");
let sidebarList = document.querySelectorAll(".sidebar li");
let searchBar = document.querySelector(".search-bar");
let notification = document.querySelector(".notification");
let search = document.querySelector(".search");
// adding event listener to add media queries
let classAdded = false;
let btnClicked = false;
window.addEventListener("resize",()=>{
    if(window.innerWidth <= 1180){
        // add class
        sidebar.classList.add("sidebar-shrink")
        classAdded = true;
    }
    else if(window.innerWidth >=1184){
        // remove class only when the button is not clicked 
        if(!btnClicked){
            sidebar.classList.remove("sidebar-shrink")
            classAdded = false;
        }
    }
})



let previous = null;
let borderActive = null;
function shrinkAndBorder(el){
    el.addEventListener("click",()=>{
        // checking whether the previous element and current are same 
        if(previous == el){
            if(window.innerWidth >= 1184){
                sidebar.classList.remove("sidebar-shrink");
            }
            classAdded = false; // because class is removed 
            btnClicked = false; // because i am unclicking it
            previous = null; // because value matched 
            el.classList.remove("border");
            search.classList.remove("search-active");
            borderActive = null;
            return;
        }
        // agar class  add nhi h toh krdo
        else if(!classAdded){
            sidebar.classList.add("sidebar-shrink");
            previous = el;
            btnClicked = true;
            search.classList.add("search-active");
            classAdded = true;
        }
        else{
            // if class is already added 
            previous = el;
            btnClicked = true; 
            search.classList.add("search-active");
        }
        sidebarList.forEach(el=>{
                // remove krna h border 
                removeBorder(el);
        })
        // now the last step add the border on the current item
        el.classList.add("border");
        borderActive = el;
    
    });
}
function removeBorder(el){
    el.classList.remove("border");
}
let arr = [searchBar,notification];
arr.forEach(el=>{   
    el.addEventListener("click",() => shrinkAndBorder(el));
});
sidebarList.forEach((el,idx)=>{
    el.addEventListener("click",()=>{
        if(el!=searchBar && el!=notification){
            // remove the border
            console.log(`idx: ${idx}`);
            removeBorder(borderActive);
            borderActive = null;
        }
        console.log(idx);
    })
})