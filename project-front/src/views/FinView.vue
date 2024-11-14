<template>
  <v-main>
    <v-container>
      <h1>금융 상품</h1>
      <v-data-table :headers="headers" :items="items" class="stock-table" hide-default-footer>
        <template #item.change="{ item }">
          <span :class="{ positive: item.change > 0, negative: item.change < 0 }">{{ item.change }}%</span>
        </template>
      </v-data-table>
    </v-container>
  </v-main>
</template>

<script setup>
import { ref } from "vue";

const headers = [
  { text: "자산명", value: "name", align: "start" },
  { text: "종목 코드", value: "code" },
  { text: "1일 상승률", value: "change" },
  { text: "1개월", value: "month1" },
  { text: "3개월", value: "month3" },
  { text: "6개월", value: "month6" },
  { text: "1년", value: "year1" },
  { text: "시가 총액", value: "market_cap" },
];

const items = ref([
  { name: "도지코인", code: "DOGE/KRW", change: 110.06, month1: 251.42, month3: 296.94, month6: 162.08, year1: 446.76, market_cap: "-" },
  { name: "크로노스", code: "CRO/KRW", change: 77.68, month1: 113.35, month3: 83.92, month6: 30.08, year1: 62.09, market_cap: "-" },
  { name: "수이", code: "SUI/KRW", change: 49.47, month1: 71.05, month3: 319.56, month6: 216.83, year1: 477.21, market_cap: "-" },
  // 추가 데이터 작성
]);
</script>

<style scoped>
.stock-table {
  font-size: 16px;
}

.positive {
  color: #e74c3c; /* 빨간색 (상승) */
}

.negative {
  color: #3498db; /* 파란색 (하락) */
}
</style>
