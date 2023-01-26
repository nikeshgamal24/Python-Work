Chart.defaults.font.size = 30;
const inputContainer = document.getElementById('input-container')

const section_a = document.getElementById('section_a')
const section_b = document.getElementById('section_b')
const section_c = document.getElementById('section_c')
const section_d = document.getElementById('section_d')
const  initial_price= document.getElementById('initial_price')

const usection_a = document.getElementById('usection_a')
const usection_b = document.getElementById('usection_b')
const usection_c = document.getElementById('usection_c')
const usection_d = document.getElementById('usection_d')
const uinitial_price= document.getElementById('uinitial_price')

const btn = document.getElementById('btn')


const stableChart = function (stableDataset,stableLabels){
    var ctx = document.getElementById('cobweb-stable').getContext('2d');
    
    new Chart(ctx, {
        type: 'line',
        data: {
            labels: stableLabels,
            datasets: [{
                label: 'Stable Market',
                backgroundColor: 'blue',
                borderColor: 'red',
                data: stableDataset
            }]
        },
        options: {
            animations: {
            tension: {
              duration: 1000,
              easing: 'linear',
              from: 1,
              to: 0,
              loop: true
            }
          },
        responsive:false,
        plugins:{
            title:{
                display:true,
                text:"Fluctuation of Market Price",
                position:"bottom",
            },
            legend:{
                display: true,
                position: "bottom",
                align: "center",
                labels:{
                    fontWeight: 'bold',
                    color : 'purple',
                }
            },
        },
     }
    });
    
}

const unStableChart = function (unStableDataset,unStableLabels){
    var ctx = document.getElementById('cobweb-unstable').getContext('2d');
    
    new Chart(ctx, {
        type: 'line',
        data: {
            labels: unStableLabels,
            datasets: [
            {
                label: 'Unstable Market',
                backgroundColor: 'green',
                borderColor: 'yellow',
                data: unStableDataset
            }]
        },
        options: {
            animations: {
            tension: {
              duration: 1000,
              easing: 'linear',
              from: 1,
              to: 0,
              loop: true
            }
          },
        responsive:false,
        plugins:{
            title:{
                display:true,
                text:"Fluctuation of Market Price",
                position:"bottom",
            },
            legend:{
                display: true,
                position: "bottom",
                align: "center",
                labels:{
                    fontWeight: 'bold',
                    color : 'purple',
                }
            },
        },
     }
    });
    
}

const gather_data = function (){
    let stableDataset = []
    let unStableDataset = []
    let stableLabels = []
    let unStableLabels = []
    noOfPoint = 25
    inputContainer.style.display = 'none'
    let a,b,c,d,p,una,unb,unc,und,unp;
    
    a = section_a.value;
    b = section_b.value;
    c = section_c.value;
    d = section_d.value;
    sp= initial_price.value;

    una = usection_a.value;
    unb = usection_b.value;
    unc = usection_c.value;
    und = usection_d.value;
    unp= uinitial_price.value;

    for(let i = 0;i<noOfPoint;i++){
        // S = c+d*p-1
        // D = a-b*p
        // D = S
        // console.log(p)
         pminus1 = sp
         sp = (a-c-(d*pminus1))/b
        //  console.log(p)
        stableDataset.push(parseFloat(sp.toFixed(2)))
        stableLabels.push(i+1)
    }
    for(let i = 0;i<noOfPoint;i++){
         pminus1 = unp
         unp = (una-unc-(und*pminus1))/unb
        //  console.log(p)
        unStableDataset.push(parseFloat(unp.toFixed(2)))
        unStableLabels.push(i+1)
    }
    console.log(stableLabels)
    console.log(unStableLabels)
    console.log(stableDataset)
    console.log(unStableDataset)
    // drawLineChart(stableDataset,unStableDataset,labels)
    stableChart(stableDataset,stableLabels)
    unStableChart(unStableDataset,unStableLabels)
}

btn.addEventListener('click',gather_data)