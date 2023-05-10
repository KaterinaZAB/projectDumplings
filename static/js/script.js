const filterBox = document.querySelectorAll('.box');
console.log(document.querySelector('nav'));
document.querySelector('nav').addEventListener('click',event => {
    if(event.target.tagName!=='LI') return false;
    let filterClass = event.target.dataset['f'];
    console.log(event.target.tagName);
    console.log(filterClass);

    filterBox.forEach( elem => {
        elem.classList.remove('hide');
        if(!elem.classList.contains(filterClass) && filterClass!=='ALL'){
            elem.classList.add('hide');
        }
    });
    
});