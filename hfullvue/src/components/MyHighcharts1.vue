<template>
    <div>
        <highcharts :options="chartOptions"></highcharts>
    </div>

</template>

<script>
    export default {
        name: "myHighcharts",
        // props: ['mydata', 'dataInfo'],
        props: ['number', 'mydata', 'dataInfo'],
        data() {
            return {
                own: false,
                chartOptions: {
                    series: [],
                    responsive: {
                        rules: [{
                            condition: {
                                maxWidth: 500
                            },
                            chartOptions: {
                                legend: {
                                    layout: 'horizontal',
                                    align: 'center',
                                    verticalAlign: 'bottom'
                                }
                            }
                        }]
                    },
                    plotOptions: {
                        series: {
                            label: {
                                connectorAllowed: false
                            },
                            pointStart: 1
                        }
                    },
                    title: {
                        text: 'Captured data details show'
                    },

                    subtitle: {
                        text: 'No.x/100'
                    },

                    yAxis: {
                        title: {
                            text: 'Number of data'
                        }
                    },

                    xAxis: {
                        accessibility: {
                            rangeDescription: 'Range: 1 to 100'
                        }
                    },

                    legend: {
                        layout: 'vertical',
                        align: 'right',
                        verticalAlign: 'middle'
                    },
                },
            }
        },
        created(){
            // this.test();
            this.generate_chart();
        },
        methods:{
            test(){
                window.console.log('number >>>>',this.number);
                for(let item in this.dataInfo){
                    window.console.log(item, this.dataInfo[item])
                }
                window.console.log('*******************************')
            },
            generate_chart(){
                let Per = this.dataInfo.itemsPer,
                    Size = this.dataInfo.array_size,
                    startNo, endNo, End,
                    starts=this.number*Per+1, ends=this.number*Per + Per;
                startNo = starts<=Size?starts:'';
                endNo = ends<=Size?ends:startNo?Size:'';
                End = (endNo==ends || ends==Size)?Per:endNo%Per;
                window.console.log('--2--', Size, startNo, endNo, Per,End, this.number);
                if (endNo > Size) {
                    endNo = Size
                }
                this.chartOptions.subtitle.text = 'Random Array No.' + startNo + '-No.' + endNo;
                window.console.log('--3--', this.own);

                //图标数据参数
                for (let i = 0; i < End; i++) {
                    let temp = new Object();
                    temp.data = this.mydata[startNo + i - 1];
                    // temp.name = 'No.' + (startNo + i);
                    temp.name = `No.${startNo + i}：[${temp.data}]`;
                    this.chartOptions.series.push(temp);
                    this.own=true;
                }
            }
        },

    }

</script>

<style scoped>

</style>