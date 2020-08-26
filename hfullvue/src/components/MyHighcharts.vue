<template>
        <div class="col-xs-6 col-md-6">
            <highcharts :options="chartOptions" v-if="own"></highcharts>
            <p  v-for="(items, index) in chartOptions.series" :key="index" aria-hidden="true" class="highcharts-description highcharts-linked-description">
                <span>{{items.name}}:<code>{{items.data}}</code></span>
            </p>
        </div>

</template>

<script>
    export default {
        name: "myHighcharts",
        props: ['number', 'mydata', 'dataInfo'],
        data() {
            return {
                own: false,
                // info: {},
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
        watch: {
            mydata: function () {
                let Per = this.dataInfo.itemsPer,
                    Size = this.dataInfo.array_size,
                    startNo, endNo, End,
                    starts=this.number*Per+1, ends=this.number*Per + Per;
                startNo = starts<=Size?starts:'';
                endNo = ends<=Size?ends:Size;
                End = (endNo==ends || ends==Size)?Per:endNo%Per;

                this.chartOptions.subtitle.text = 'Random Array No.' + startNo + '-No.' + endNo;

                //图标数据参数
                if (startNo){
                    this.own=true;
                    for (let i = 0; i < End; i++) {
                        let temp = new Object();
                        temp.data = this.mydata[startNo + i - 1];
                        temp.name = 'No.' + (startNo + i);
                        // temp.name = `No.${startNo + i}：[${temp.data}]`;
                        // this.info[`No.${startNo + i}：`]=`[${temp.data}]`;
                        this.chartOptions.series.push(temp);
                    }
                }

            }
        },

    }

</script>

<style scoped>

</style>