function expand(id){
    var element = document.getElementById(id);
    const allother = document.getElementsByClassName("expandable");      
        for(let i = 0; i < allother.length; i++)
        {
            if(allother[i].classList.contains('expanded') && allother[i] != element)
            {
                allother[i].classList.remove('expanded');
                allother[i].classList.add('hover');
            }
        }
        if (!element.classList.contains('expanded'))
        {
            element.classList.add('expanded');
            element.classList.remove('hover');
        } else if (element.classList.contains('expanded'))
        {
            element.classList.remove('expanded');
            element.classList.add('hover');
        }
}

function findEquivalence(){
    
        let moles1 = parseFloat(document.getElementById('moles1').value);
        let moles2 = parseFloat(document.getElementById('moles2').value);

        let equivalence = moles2 / moles1 ;

        document.getElementById('equivalence').textContent = `${equivalence}.`;   
}


const quotes = ['"The meeting of two personalities is like the contact of two chemical substances: if there is any reaction, both are transformed." -Carl Gustav Jung ', '"Chemistry is like cooking... just dont lick the spoon." -anonymous','"Think like a proton and stay positive." -random chemist']
document.getElementById("quote").innerHTML = quotes[Math.floor(Math.random() * 3)]; 

