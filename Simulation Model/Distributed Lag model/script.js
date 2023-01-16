/*
C--> Consumption
I--> Investment
T--> Tax
G--> Government ependiture
Y--> National Income
*/ 
Chart.defaults.font.size = 30;
let time_stamp_container= document.getElementById("time_stamp")

const input_container = document.getElementById('input-container')

const btn = document.getElementById('btn')

const barChart = function (consumption){
    const ctx = document.getElementById('myChart');

  new Chart(ctx, {
    type: 'bar',
    data: {
      labels:time_stamp==6?['1st Year', '2nd Year', '3rd Year', '4th Year', '5th Year', '6th Year']: time_stamp==7?['1st Year', '2nd Year', '3rd Year', '4th Year', '5th Year', '6th Year', '7th Year']:['1st Year', '2nd Year', '3rd Year', '4th Year', '5th Year'],
      datasets: [{
        label: 'Growth of National Income',
        data: consumption,
        backgroundColor:time_stamp==6?["red","blue","green","purple","gold",'silver']:time_stamp==7?["red","blue","green","purple","gold",'silver','violet']:["red","blue","green","purple","gold"],
        borderWidth: 1
      }]
    },
    options: {
    responsive:false,
    plugins:{
        title:{
            display:true,
            text:"Bar Chart of Growth of National Income",
            position:"bottom",
        },
        legend:{
            display: true,
            position: "bottom",
            align: "center",
            labels:{
                fontWeight: 'bold',
                color : 'red',
                boxWidth:0,
            }
        },
    },
    animations:{
        tension:{     
        duration: 5000,
        easing: "easeInOutBounceeaseOutBounce",
        from: 1,
        to: 0,
    }
  }
  }
});
}

const display = function (){
    time_stamp = time_stamp_container.value;;
    console.log(time_stamp)
    
    //Government expenditure
    let govExpenditure = time_stamp==6?[20,25,30,35,40,45]:time_stamp==7?[20,30,20,50,40,35,45]:[20,25,30,35,40]
    let consumption = []
    let T,Y,C,I


    input_container.style.display = 'none'
    /*******Major Calculation**********/
     Y =  80;
    
    console.log(time_stamp);
    console.log(govExpenditure)

    for(let i=0;i < time_stamp;i++){
        I = 2 + 0.1 * Y
        Y = 45.45 + 2.27*(I+govExpenditure[i])
        T = 0.2*Y
        C = 20 +0.7*(Y-T)
        console.log(C)
        consumption.push(C)
    }

// console.log(consumption)
    barChart(consumption)
}
btn.addEventListener('click',display)
