function SetPath(url,path){
    request = new XMLHttpRequest();
    request.open('POST',url,true);
    request.setRequestHeader("Content-type","application/x-www-form-urlencoded");
    request.send("path="+path);
    request.onreadystatechange = function () {
        if(this.status==200){
            location.reload()
        }
    }
}