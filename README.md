<!DOCTYPE html>
<html>
<body>
    
<h1>Demo API</h1>
<h1>BestTime API - Today's foot traffic chart example</h1>
<div>
    <form>
        <label for="api_key_private">Insert here your BestTime <a target="_blank" href="https://besttime.app/api/v1/api_keys_list">private API key</a></label><br>
        <input type="text" id="api_key_private" placeholder="Your private API Key" value="pri_b944cb4fbd1148f3b083b503028c7590" />
        <p>Never use your private API key on your own public website to avoid abuse. Only use it on this page for testing purposes. Get the API data through your back-end or use the public API key in combination with a <a href="https://documentation.besttime.app/#query-week-raw">query</a> API endpoint</p>
    </form>
    <form>
        <label for="api_key_private">Type a Cafe and address and press the Forecast button</label><br>
        <input type="text" id="venue_name" placeholder="Venue Name" value="Starbucks coffee " />
        <input type="text" id="venue_address" placeholder="Venue Address" value="Kyoto Sando Tower" />
        <button id="btnForecast" type="submit">Forecast</button>
    </form>
</div>
<br>

<!-- The div where the chart will be shown. A width and heigth is required for eCharts -->
<div id="footTrafficDay" style="width:800px; height:300px;" ></div>


<p>Check out the <a href="https://blog.besttime.app/tag/tutorials/">BestTime tutorial section</a> for more information</p>
</body>
</html>

<!-- eCharts is used to generate the graph -->
<script src="https://cdn.jsdelivr.net/npm/echarts@4.7.0/dist/echarts.min.js"
integrity="sha256-eKrx6Ly6b0Rscx/PSm52rJsvK76RJyv18Toswq+OLSs=" crossorigin="anonymous"></script>

<!-- Script to get the foot traffic from the BestTime API and vizualize the data using eCharts -->
<script>

// Graph options
var option = {
    title: {
        text: "Today's foot traffic",
    },
    tooltip: {
        show: true,
        formatter: '{c}% vs max <br> max of the week'
    },
    xAxis: {
        show: true,
        nameTextStyle: {
        color: "#b5b5b5"
        },
        axisLine: {
        show: false
        },
        axisTick: {
        show: false
        },
        axisLabel: {
        show: true,
        showMinLabel: true,
        showMaxLabel: true,
        interval: 3,
        color: "#b5b5b5",
        align: 'center'
        },
        //   nameGap: 40,
        data: ['6AM', '7AM', '8AM', '9AM', '10AM', '11AM', '12PM', '1PM', '2PM', '3PM', '4PM', '5PM', '6PM',
        '7PM', '8PM', '9PM', '10PM', '11PM', '12AM', '1AM', '2AM', '3AM', '4AM', '5AM']
    },
    yAxis: {
        show: true,
        min: 0,
        max: 100,
        interval: 100,
        // name: "Busyness",
        // nameLocation: 'middle',
        // nameTextStyle: {
        //     color: "#b5b5b5"
        // },
        axisLine: {
        show: false
        },
        axisTick: {
        show: false,
        },
        axisLabel: {
        show: true,
        interval: 100,
        showMaxLabel: true,
        showMinLabel: false,
        color: "#b5b5b5",
        // align: 'left',
        formatter: function (value) {
            return value + "%";
        }
        },
        splitline: {
        show: false
        }
    },
    grid: {
        left: 40,
        top: 30,
        right: 0,
        bottom: 20
    },
    series: [{
        type: 'bar'
    }]
};

// Preconfig chart with basic options
// Based on prepared DOM, initialize echarts instance
var chartToday = echarts.init(document.getElementById("footTrafficDay"));
chartToday.setOption(option);
chartToday.showLoading({
    text: 'Insert your private API key and press the Forecast button',
});



// let data;
// let dataToday;
// let dataLive;

// Find the current day of the week to show only today's 
const d = new Date();
// Javascript getDay returns 0-6 where 0 is Sunday and 6 is Saturday
// BestTime API returns 0-6 where 0 is Monday and 6 is Sunday
let dayInt =  d.getDay() < 6 ? d.getDay() + 1 : 0;
console.log(dayInt);

function getFootTrafficData() {

    const params = new URLSearchParams({ 
    'api_key_private': document.getElementById("api_key_private").value,
    'venue_name': document.getElementById("venue_name").value,
    'venue_address': document.getElementById("venue_address").value
    });

    fetch(`https://besttime.app/api/v1/forecasts?${params}`, {
    method: 'POST'
    }).then((response) => response.json())
    .then((data) => {
        document.getElementById("btnForecast").disabled = false;

        if (data.status == "error") {

        if ('message' in data) {
            console.log();
            if ('api_key_private' in data) {
                alert(JSON.stringify(data.message.api_key_private[0]))
            } else {
                alert(JSON.stringify(data.message))
                console.log(data.message)
            }
        }
        } else {
            dataToday = data['analysis'][dayInt.toString()]

            // Show all foot traffic forecast percentages in the console from 6AM until 5AM next morning.
            console.log(dataToday);

            chartToday.hideLoading();
            chartToday.setOption({
                title: {
                    text: "Today's foot traffic for " + data.venue_info.venue_name + " " + data.venue_info.venue_address,
                },
                series: [{
                name: "Forecasted busyness",
                clip: false,
                type: 'bar',
                itemStyle: {
                    color:"#7dabf4"
                },
                z: 0,
                data: dataToday.day_raw
                }]});

        }

    })
    .catch(console.error);

    // Add Live data to the same chart
    fetch(`https://besttime.app/api/v1/forecasts/live?${params}`, {
    method: 'POST'
    }).then((response) => response.json())
    .then((dataLive) => {

        // Show all live data in the console
        console.log(dataLive);

        if (dataLive.status == "OK") {

            pct = dataLive.analysis.venue_live_busyness;

            // Scale yaxis higher if we have a live number higher than 100%
            if (pct > 100) {
                yaxisMax = pct
            } else {
                yaxisMax = 100;
            }

            if (pct > 80) {
                liveLabelOffsetHor = 30;
            } else {
                liveLabelOffsetHor = -5;
            }

            // If 5am adjust x-axis to prevent a day wide live bar
            hour_start_12 = dataLive.analysis.hour_start_12
            hour_end_12 = dataLive.analysis.hour_end_12
            if (hour_start_12 == "5AM") {
                hour_end_12 = "";
            }

            // Includes duplicate code for yAxis, this is done on purpose
            chartToday.setOption({
                yAxis: {
                    show: true,
                    min: 0,
                    max: yaxisMax,
                    axisLine: {
                    show: false
                    },
                    axisTick: {
                    show: false,
                    },
                    axisLabel: {
                    show: true,
                    interval: 100,
                    showMaxLabel: true,
                    showMinLabel: false,
                    color: "#b5b5b5",
                    // align: 'left',
                    formatter: function (value) {
                        return value + "%";
                    }
                    }
                },
                series: [{
                    "name": "Live busyness",
                    "markArea": {
                    "label": {
                        "show": true,
                        "position": [liveLabelOffsetHor, "100%"],
                        "offset": [0, -210],
                        "fontSize": 20,
                        "color": 'white',
                        "backgroundColor": "#f50057",
                        "distance": 'top'
                    },
                    "silent": false,
                    "data": [
                        [{
                        "name": "Live",
                        //"type": 'min',
                        "yAxis": 0,
                        "value": pct,  //Live value tooltip.
                        "xAxis": hour_start_12,
                        "itemStyle": {
                            "color": "#f50057",
                            "shadowBlur": 30,
                            "shadowOffsetX": 1,
                            "opacity": 0.5
                        }
                        }, {
                        "yAxis": pct,
                        "xAxis": hour_end_12,
                        }]
                    ]
                    }
                }]
                });

        }

    })
    .catch(error => {
        console.error;
        document.getElementById("btnForecast").disabled = false;
    });
}

// Load on page load
//getFootTrafficData();

// Reload the forecast data when clicking the Forecast button
document.getElementById("btnForecast").addEventListener('click', (event) => {
    event.preventDefault();

    document.getElementById("btnForecast").disabled = 'true';

    getFootTrafficData();
});









// Generate the foot traffic chart




// $.ajax(api_settings("forecasts/day/raw", {
//         "day_int": data.analysis.day_info.day_int,
//         // Get api_key_public value from the URL parameter
//         "api_key_public": urlParam('api_key_public'),
//         // Get venue_id value from the URL parameter and decode it
//         "venue_id": decodeURIComponent(urlParam('venue_id'))
//       },"GET")).done(function (data) {

//         $("#api_results_dayraw").text(JSON.stringify(data, null, "\t"));

//         myChart.setOption({
//           series: [{
//           name: "Forecasted busyness",
//           clip: false,
//           type: 'bar',
//           itemStyle: {
//               color:"#7dabf4"
//           },
//           z: 0,
//           data: data.analysis.day_raw
//         }]});

//         // new ApexCharts(document.querySelector("#chart-day-overview"),
//         //   chartPlotDayRaw(data.analysis.day_raw, "Busyness %")).render();

//         //Resize so card heights will still match after new API data
//         $("body").resize();
//       });


</script>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Cafe-desu</title>
</head>
<body>
    <header>
        <h1>Welcome to Cafe-desu</h1>
    </header>

    <section>
        <h2>Concept</h2>
        <p>- User can earn all the info about the cafe from our website</p>
        <p>- Easy to confirm crowdedness, distance, open/close, estimated seat availability</p>
        <p>- Target Market: People who want to talk in Cafe, who need a beverage, who wants to study/work</p>
        <p>- Selecting a popular Cafe within a two-kilometer radius of Kyoto Station</p>
        <p>- Recommendation systems using Keyword-based Matching to find the Cafe</p>
    </section>

    <section>
        <h2>Professor advice: MAKE IT FUNNIER!!</h2>
        <p>(Add funny and features here)</p>
    </section>

    <section>
        <h2>Elements for Website</h2>
        <ul>
            <li>Cafe open/close</li>
            <li>If it is crowded or not (Red, Yellow, Green)</li>
            <li>How long the user can stay</li>
            <li>User review</li>
            <li>Distance of Cafe</li>
            <li>Estimated seat availability</li>
            <li>Cost</li>
            <li>Non-smoking seat</li>
        </ul>
    </section>

    <section>
        <h2>Keywords for Researching Cafe</h2>
        <ul>
            <li>WiFi</li>
            <li>Study</li>
            <li>Able to charge the devices or not</li>
            <li>Seat availability</li>
            <li>Include lunch</li>
            <li>Include breakfast</li>
            <li>Long stay</li>
            <li>Talking</li>
            <li>Mysterious</li>
            <li>New</li>
        </ul>
    </section>

    <section>
        <h2>Data Collection</h2>
        <p>Physical: can study or not (time that we can study) Whether it is possible to study and whether there are restrictions on study time.</p>
        <p>Using API from BestTime.app</p>
    </section>

    <section>
        <h2>Finding Cafe (Near Kyoto Station)</h2>
        <p>For public open spaces in Kyoto, we want to make an application that locates where the nearest Famous Cafe in Kyoto has certainly available slots. This is to study/ public open spaces to focus. Since most of the time, Starbucks is very crowded and full.</p>
        <p>Data collection: Data on the congestion in Starbucks by using API</p>
    </section>

    <section>
        <h2>Literature Review Topic</h2>
        <ul>
            <li>study environment and productivity in cafe(Daiki)</li>
            <li>Query Expansion and Reformulation(Baizid)</li>
            <li>Analysis of reviews and evaluation data and reliability assessment(Rei)</li>
            <li>Recommendation systems reflecting user needs and preferences for restaurants</li>
            <li>Keyword-based Search and Matching(Eiji)</li>
            <li>pedestrian indoor localization smartphone sensors(Kevin)</li>
            <li>store location accessibility(Daiki)</li>
        </ul>
    </section>
</body>
</html>

