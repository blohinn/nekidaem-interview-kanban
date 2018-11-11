<template>
  <div class="kanban-card">
    <p class="mb-0"><span style="color: white"><b>id:</b></span> 123456</p>
    <p class="mb-0">Lorem ipsum dolor</p>
  </div>
</template>

<script>
  export default {
    name: "Card"
  }
</script>

<style scoped>
  .kanban-card {
    background-color: #1F1F22;
    padding: 10px;
  }

  .kanban-card:not(:first-child) {
    margin-top: 10px;
  }
</style>
