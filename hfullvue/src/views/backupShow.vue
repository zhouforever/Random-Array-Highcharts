<template>
    <div>
        <div class="container">

            <h2 id="line-charts">Backup_show <small>No.1: Latest data</small></h2>
            <div class="row">
                <div class="bs-example" data-example-id="simple-thumbnails">
                        <div class="row">
                            <MyHighcharts :mydata="data_store" :dataInfo="data_info" :number="0"></MyHighcharts>
                            <MyHighcharts :mydata="data_store" :dataInfo="data_info" :number="1"></MyHighcharts>
                            <MyHighcharts :mydata="data_store" :dataInfo="data_info" :number="2"></MyHighcharts>
                            <MyHighcharts :mydata="data_store" :dataInfo="data_info" :number="3"></MyHighcharts>
                            <MyHighcharts :mydata="data_store" :dataInfo="data_info" :number="4"></MyHighcharts>
                            <MyHighcharts :mydata="data_store" :dataInfo="data_info" :number="5"></MyHighcharts>
                            <MyHighcharts :mydata="data_store" :dataInfo="data_info" :number="6"></MyHighcharts>
                            <MyHighcharts :mydata="data_store" :dataInfo="data_info" :number="7"></MyHighcharts>
                            <MyHighcharts :mydata="data_store" :dataInfo="data_info" :number="8"></MyHighcharts>
                            <MyHighcharts :mydata="data_store" :dataInfo="data_info" :number="9"></MyHighcharts>
                            <MyHighcharts :mydata="data_store" :dataInfo="data_info" :number="10"></MyHighcharts>
                            <MyHighcharts :mydata="data_store" :dataInfo="data_info" :number="11"></MyHighcharts>
                            <MyHighcharts :mydata="data_store" :dataInfo="data_info" :number="12"></MyHighcharts>
                            <MyHighcharts :mydata="data_store" :dataInfo="data_info" :number="13"></MyHighcharts>
                            <MyHighcharts :mydata="data_store" :dataInfo="data_info" :number="14"></MyHighcharts>
                            <MyHighcharts :mydata="data_store" :dataInfo="data_info" :number="15"></MyHighcharts>
                            <MyHighcharts :mydata="data_store" :dataInfo="data_info" :number="16"></MyHighcharts>
                            <MyHighcharts :mydata="data_store" :dataInfo="data_info" :number="17"></MyHighcharts>
                            <MyHighcharts :mydata="data_store" :dataInfo="data_info" :number="18"></MyHighcharts>
                            <MyHighcharts :mydata="data_store" :dataInfo="data_info" :number="19"></MyHighcharts>
                        </div>
                    <!--</div>-->

                </div>
            </div>

        </div>
    </div>
</template>

<script>
    import MyHighcharts from "@/components/MyHighcharts"

    export default {
        name: "Backup_show",
        data() {
            return {
                data_store: [],
                data_info:{
                    array_size: 0,
                    itemsPer: 5,
                },
            }
        },
        created() {
            this.data_show()
        },
        methods: {
            data_show() {
                this.$axios({
                    url: this.$settings.Host + 'backup_show/',
                    method: 'get',
                }).then(response => {
                    this.data_store = response.data;
                    this.data_info.array_size=response.data.length;
                })
            }
        },
        components: {
            MyHighcharts,
        },
    }

</script>

<style scoped>
    div MyHighcharts{
        margin: 10px;
        background-color: #f1f7ff;
    }
</style>