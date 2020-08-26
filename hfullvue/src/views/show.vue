<template>
    <div>
        <div class="container">
            <h2 id="line-charts">Backup_show <small>No.1: Latest data</small></h2>

            <div class="row">
                <div class="bs-example" data-example-id="simple-thumbnails">
                    <div class="row">
                        <div v-for="(item,index) in data_info.chartsTotal" :key="item" @change=get_orderNo(index)>
                            <div class="col-xs-6 col-md-6">Current chart No.{{index+1}}
                                <MyHighcharts :mydata="data_store" :dataInfo="data_info" :number="index"></MyHighcharts>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

        </div>
    </div>
</template>

<script>
    import MyHighcharts from "@/components/MyHighcharts1"

    export default {
        name: "Backup_show",
        data() {
            return {
                data_store: [],
                data_info: {
                    array_size: 0,
                    itemsPer: 5,
                    chartsTotal: 0,
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
                    this.data_info.array_size = response.data.length;

                    let size = response.data.length,
                        Per = this.data_info.itemsPer,
                        remainder = size % Per;
                    this.data_info.chartsTotal = (remainder == 0)
                        ? size / Per
                        : ((size - remainder) / Per + 1);

                    window.console.log('------+------->>>', this.data_info.array_size,
                        this.data_info.itemsPer, this.data_info.chartsTotal);
                })
            },
        },
        components: {
            MyHighcharts,
        },
    }

</script>

<style scoped>

</style>