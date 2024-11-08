<template>
  <v-container class="product-section">
    <h1 class="section-title">Hot</h1>

    <!-- 커스텀 탭 네비게이션 -->
    <v-card flat>
      <div class="custom-tabs">
        <div v-for="(tab, index) in tabs" :key="index" :class="['tab-item', { active: currentTab === index }]" @click="currentTab = index">
          {{ tab }}
        </div>
      </div>

      <!-- 금융 상품 테이블 -->
      <FinProductTable :current-tab="currentTab" :tabs="tabs"/>
    </v-card>
  </v-container>
</template>

<script setup>
import { ref } from "vue";
import FinProductTable from "./FinProductTable.vue";
const currentTab = ref(0);
const tabs = ["예금", "적금", "주식", "코인"];
const emit = defineEmits(["update:currentTab"]);
</script>

<style scoped>
.product-section {
  background-color: #f9fafb;
  padding: 20px;
  border-radius: 12px;
  margin-top: 20px;
}
.custom-tabs {
  display: flex;
  border-bottom: 1px solid #e2e8f0;
  margin-bottom: 1rem;
  overflow-x: auto;
  white-space: nowrap;
}

.tab-item {
  padding: 0.75rem 1.5rem;
  cursor: pointer;
  font-weight: 500;
  color: #4a5568;
  border-bottom: 2px solid transparent;
  transition: all 0.2s;
}

.tab-item.active {
  color: #2b6cb0;
  border-bottom: 2px solid #2b6cb0;
}

</style>
