<template>
    <div id="app">
        <div>
            <nav class="navbar navbar-inverse">
                <div class="container-fluid">
                    <!-- Brand and toggle get grouped for better mobile display -->
                    <div class="navbar-header">
                        <button type="button" class="navbar-toggle collapsed" data-toggle="collapse"
                                data-target="#bs-example-navbar-collapse-9" aria-expanded="false">
                            <span class="sr-only">Toggle navigation</span>
                            <span class="icon-bar"></span>
                            <span class="icon-bar"></span>
                            <span class="icon-bar"></span>
                        </button>
                        <div class="navbar-brand">HighCharts Show</div>
                    </div>

                    <!-- Collect the nav links, forms, and other content for toggling -->
                    <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-9">
                        <ul class="nav navbar-nav">
                            <li><router-link to="/">Dynamic</router-link></li>
                            <li><router-link to="/backup">Collect</router-link></li>
                            <li><router-link to="/backup1">Collect Test</router-link></li>
                        </ul>
                    </div>
                </div>
            </nav>
            &nbsp;&nbsp;

        </div>
        <router-view/>


    </div>
</template>

<script>
    export default {
        name: 'App',
        components: {},
    }
</script>

<style>
    #app {
        font-family: Avenir, Helvetica, Arial, sans-serif;
        -webkit-font-smoothing: antialiased;
        -moz-osx-font-smoothing: grayscale;
        text-align: center;
        color: #2c3e50;
        margin-top: 60px;
    }
</style>
