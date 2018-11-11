<template>
  <div class="column">

    <div class="column-header">
      <p class="ml-2 mb-0">Header title</p>
    </div>

    <div class="column-content">
      <card v-for="c in cards" :key="c"></card>
    </div>
  </div>
</template>

<script>
  import Card from '@/components/kanban/Card'

  export default {
    name: "Column",
    components: {
      Card
    },
    data() {
      return {
        cards: [
          1,
          2,
          3,
          4
        ]
      }
    }
  }
</script>

<style scoped>
  .column {
    white-space: normal;
    width: 300px;
    margin-top: 30px;
    margin-right: 50px;
    margin-bottom: 30px;
    display: inline-block;
  }

  .column:first-child {
    margin-left: 30px;
  }

  .column-header {
    background-color: red;
    color: white;
    text-shadow: 0 0 4px #4b5263;
    text-transform: uppercase;
    font-size: 18px;
    font-weight: 200;
    margin: 0;
    padding: 10px;
  }

  .column-content {
    background-color: #2b2d33;
    color: rgba(255, 255, 255, 0.53);
    padding: 10px 10px 10px 10px;
  }
</style>
