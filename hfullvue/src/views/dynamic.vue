<template>
    <div>

        <div class="container">
            <div class="row">
                <div class="col-md-4 base-info">
                    <h1>
                        Dynamic
                    </h1>
                    <ul type="none">
                        <li>Array: {{chartOptions.series[0].data}}</li>
                        <li>Length: {{chartOptions.series[0].data.length}}</li>
                        <li>Interval: {{interval}}&nbsp;seconds</li>
                        <li>Generate Time: {{time}}</li>
                        <li>Note: when the webpage is refreshed, the data is updated and the timing starts</li>
                    </ul>
                </div>
                <div class="col-md-8">
                    <div class="jumbotron">
                        <h2>Latest data trends</h2>
                        <div>
                            <highcharts :options="chartOptions"></highcharts>
                        </div>
                        <p><span @click="grab_data" class="btn btn-primary btn-lg" role="button">Grab data</span></p>
                    </div>
                </div>

            </div>
        </div>


    </div>
</template>


<script>
    export default {
        data() {
            return {
                time: 'Y-m-d H:M:s',
                interval:10,
                chartOptions: {
                    title: {
                        text: 'Current data show'
                    },
                    series: [{
                        name: 'Data trend curve',
                        data: [ 54, 81, 4, 66, 91, 37 ]
                    }]
                }
            }
        },
        created() {
        },
        methods: {
            get_data() {
                this.$axios.get(`${this.$settings.Host}dynamic/`).then(response => {
                    window.console.log('/*/*/:', response.data);
                    if (response) {
                        this.chartOptions.series[0]['data'] = response.data;
                    }
                })
            },
            grab_data(){
                if (this.time!='Y-m-d H:M:s'){
                    this.$axios({
                        url: this.$settings.Host + 'backup/',
                        method: 'post',
                        data: {
                            'array': this.chartOptions.series[0]['data']
                        }
                    }).then((response)=> {
                        this.$alert.Alert(response.data);
                        // window.alert(response.data)
                    })
                }else{
                    this.$alert.Alert('Test data, please wait ...');
                    // window.alert('Test data, please wait ...');
                }

            },
            get_time(){
                let CurrentTime= new Date();
                let year = CurrentTime.getFullYear(),
                    month = CurrentTime.getMonth()+1,
                    date = CurrentTime.getDate(),
                    hour = CurrentTime.getHours(),
                    minutes = CurrentTime.getMinutes(),
                    seconds = CurrentTime.getSeconds();
                let MyTime = `
                    ${year}-${month}-${date} ${hour}:${minutes}:${seconds}
                    `;
                this.time=MyTime;
            },
        },
        mounted() {
            //立即执行
            setTimeout(this.get_data, 0);
            setTimeout(this.get_time, 0);
            //每隔10秒刷新一次图表数据
            window.setInterval(() => {

                setTimeout(this.get_data, 0);
                setTimeout(this.get_time, 0);
            }, 1000*this.interval);
        },

    }
</script>
