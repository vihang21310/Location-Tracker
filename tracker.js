const track = ()=>{
    const status = document.querySelector('.status')

    const success = (position)=>{
        console.log(position)
        const latitude = position.coords.latitude;
        const longitude = position.coords.longitude;
        var txtOutput = document.getElementById("txtOutput");
  
      txtOutput.value = `${"Lat:"+ latitude +' '+ "Lng:"+longitude } Date: ${date}`
        console.log(`${x} your current location is :`+latitude +' '+ longitude + " "+"Date:" + date)
    }
    const error = ()=>{
        status.textContent = 'unable to retrive your location'

    }
    navigator.geolocation.getCurrentPosition(success,error)
}
var today = new Date();

var date = today.getFullYear()+'-'+(today.getMonth()+1)+'-'+today.getDate();
x = document.getElementById("myText").value
const tracking = setInterval(track,90000)
document.querySelector('.btn').addEventListener('click',track)



