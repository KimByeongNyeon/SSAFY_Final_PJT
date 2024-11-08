<template>
  <v-data-table :headers="getHeaders" :items="getItems" hide-default-footer class="financial-table">
    <!-- 종목명/상품명 열 커스텀 템플릿 -->
    <template v-slot:item.name="{ item }">
      <div class="d-flex align-center">
        <v-avatar size="24" class="mr-2">
          <v-img :src="item.image || 'https://via.placeholder.com/24'" />
        </v-avatar>
        <div>
          <div class="font-weight-medium">{{ item.name }}</div>
          <div class="caption grey--text">{{ item.code }}</div>
        </div>
      </div>
    </template>

    <!-- 등락률/이자율 열 커스텀 템플릿 -->
    <template v-slot:item.change="{ item }">
      <span :class="getChangeClass(item.change)">{{ item.change >= 0 ? "+" : "" }}{{ item.change }}%</span>
    </template>

    <!-- 거래량 열 커스텀 템플릿 -->
    <template v-slot:item.volume="{ item }">
      {{ numberFormat(item.volume) }}
    </template>

    <!-- 금액 열 커스텀 템플릿 -->
    <template v-slot:item.price="{ item }">
      {{ numberFormat(item.price) }}
    </template>
  </v-data-table>
</template>

<script setup>
import { numberFormat, getChangeClass } from "@/utils/fomatters";
import { computed } from "vue";
const props = defineProps({
  currentTab: Number,
  tabs: Array,
});

const headers = {
  stock: [
    { text: "종목명", value: "name", align: "start" },
    { text: "현재가", value: "price", align: "end" },
    { text: "전일비", value: "priceChange", align: "end" },
    { text: "등락률", value: "change", align: "end" },
    { text: "거래량", value: "volume", align: "end" },
    { text: "거래대금", value: "tradingValue", align: "end" },
    { text: "시가총액", value: "marketCap", align: "end" },
  ],
  deposit: [
    { text: "상품명", value: "name", align: "start" },
    { text: "은행", value: "bank", align: "start" },
    { text: "금리", value: "change", align: "end" },
    { text: "최소가입금액", value: "minAmount", align: "end" },
    { text: "가입기간", value: "period", align: "end" },
  ],
  savings: [
    { text: "상품명", value: "name", align: "start" },
    { text: "은행", value: "bank", align: "start" },
    { text: "금리", value: "change", align: "end" },
    { text: "월 납입액", value: "monthlyPayment", align: "end" },
    { text: "가입기간", value: "period", align: "end" },
  ],
  crypto: [
    { text: "암호화폐", value: "name", align: "start" },
    { text: "현재가", value: "price", align: "end" },
    { text: "전일비", value: "priceChange", align: "end" },
    { text: "등락률", value: "change", align: "end" },
    { text: "거래량", value: "volume", align: "end" },
    { text: "시가총액", value: "marketCap", align: "end" },
  ],
};

// 샘플 데이터
const items = {
  stock: [
    {
      name: "삼성전자",
      code: "005930",
      price: 57300,
      priceChange: -300,
      change: -0.52,
      volume: 21933484,
      tradingValue: 1253062,
      marketCap: 3438595,
    },
    {
      name: "SK하이닉스",
      code: "000660",
      price: 195800,
      priceChange: 2600,
      change: 1.35,
      volume: 3418604,
      tradingValue: 670697,
      marketCap: 1406501,
    },
  ],
  deposit: [
    {
      name: "프리미엄 정기예금",
      bank: "신한은행",
      code: "SH001",
      change: 4.5,
      minAmount: 10000000,
      period: "12개월",
    },
    {
      name: "디지털 정기예금",
      bank: "국민은행",
      code: "KB001",
      change: 4.3,
      minAmount: 5000000,
      period: "24개월",
    },
  ],
  savings: [
    {
      name: "청년우대적금",
      bank: "우리은행",
      code: "WR001",
      change: 5.2,
      monthlyPayment: 500000,
      period: "36개월",
    },
    {
      name: "직장인적금",
      bank: "하나은행",
      code: "HN001",
      change: 4.8,
      monthlyPayment: 1000000,
      period: "24개월",
    },
  ],
  crypto: [
    {
      name: "비트코인",
      code: "BTC",
      price: 68000000,
      priceChange: 1500000,
      change: 2.25,
      volume: 5234567,
      marketCap: 1234567890,
    },
    {
      name: "이더리움",
      code: "ETH",
      price: 3500000,
      priceChange: -50000,
      change: -1.41,
      volume: 3456789,
      marketCap: 987654321,
    },
  ],
};
const tabToKey = {
  예금: "deposit",
  적금: "savings",
  주식: "stock",
  코인: "crypto",
};

const getHeaders = computed(() => {
  const key = tabToKey[props.tabs[props.currentTab]];
  return headers[key];
});

const getItems = computed(() => {
  const key = tabToKey[props.tabs[props.currentTab]];
  return items[key];
});
</script>

<style scoped>
/* 테이블 스타일 */
.financial-table {
  background: white;
  border-radius: 8px;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
}

.financial-table >>> .v-data-table__wrapper {
  margin: 0 -16px;
}

.financial-table >>> table {
  border-spacing: 0;
}

.financial-table >>> th {
  background: #f8f9fa !important;
  color: #4a5568 !important;
  font-weight: 600 !important;
  white-space: nowrap;
}

.financial-table >>> td {
  border-bottom: 1px solid #e2e8f0;
  padding: 12px 16px !important;
  font-size: 0.875rem;
}
.red--text {
  color: #ff5252;
}
.blue--text {
  color: #2196f3;
}
</style>
