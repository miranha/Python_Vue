<template>
    <div>
      <input v-model="inputValue" @keyup.enter="sendValueToBackend" placeholder="Enter a value" />
    </div>
  </template>
  
  <script>
  import axios from 'axios'

  export default {
    data() {
      return {
        inputValue: ''
      }
    },
    methods: {
      sendValueToBackend() {
        axios.post('http://localhost:5000/value', { value: this.inputValue })
          .then(response => {
            console.log("Value entered")
            console.log(response.data + " yo")
          })
          this.inputValue = ''
      }
    }
  }
  </script>
  