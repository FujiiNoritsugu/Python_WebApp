function check_input(){
    table_obj = document.getElementById('table_id');
    if (is_red){
        table_obj.style.backgroundColor = "red";
        is_red = false;
    }else{
        table_obj.style.backgroundColor = "";
        is_red = true;
    }
}
