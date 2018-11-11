<template>
  <div id="board">

    <div class="kanban-row">
      <column v-for="c in columns" :key="c"></column>
    </div>

  </div>
</template>

<script>
  import Column from '@/components/kanban/Column'

  export default {
    name: "Board",
    components: {
      Column
    },
    data() {
      return {
        columns: [
          1,
          2,
          3,
          4,
          5,
          6
        ]
      }
    }
  }
</script>

<style>
  #board {
    background-color: #35383f;
    margin: 0;
    padding: 0 0 0 0;
    height: 100%;
  }
  .kanban-row {
    overflow-x: scroll;
    white-space: nowrap;
    height: 100%;
  }
</style>
