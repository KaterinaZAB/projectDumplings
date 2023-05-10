$(document).ready(function(){
    let counter=1;
    let length=$(".slide").length;

    $('.next').click(function(e){
        if($(':animated').length){
            return false;
        }
        if(counter==length){
            counter=0;
        }
        let perc=100*counter;
        $('.container').animate({
            marginLeft:"-"+perc+"%"
        },2000,()=> {
            counter++;
        });
    });
    $('.prev').click(function(e){
        if($(':animated').length){
            return false;
        }
        if(counter==1){
            counter=length-1;

        let perc=100*counter;
        $('.container').animate({
            marginLeft:"-"+perc+"%"
        },2000,()=> {
            counter++;
        });
        return;
    }
        let perc=100 * counter;
        $('.container').animate({
            marginLeft:"-"+(perc-200)+"%"
        },2000,() => {
            counter--;
        });
    });
})
    