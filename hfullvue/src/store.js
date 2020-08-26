import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
      course_id:0  //仓库传参 跳转4
  },
  mutations: {
    set_course_id(state, new_value){
        state.course_id = new_value
    }
  },
  actions: {

  }
})
