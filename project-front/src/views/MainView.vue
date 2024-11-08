<template>
  <v-app>
    <NavBar />
    <MainPageCarousel :slides="carouselSlides" />
    <MainPageFinProduct :tabs="tabs" :currentTab="currentTab" :headers="getHeaders" :items="getItems" @update:currentTab="currentTab = $event" />
    <Footer />
  </v-app>
</template>

<script setup>
import Footer from "@/components/Footer.vue";
import MainPageCarousel from "@/components/MainPageCarousel.vue";
import MainPageFinProduct from "@/components/MainPageFinProduct.vue";
import NavBar from "@/components/NavBar.vue";
import { ref, computed } from "vue";

const currentTab = ref(0);
const tabs = ["예금", "적금", "주식", "코인"];

// 캐러셀 데이터
const carouselSlides = [
  {
    image: "https://via.placeholder.com/1200x400",
    title: "금융 상품 추천",
    subtitle: "당신을 위한 맞춤 금융 상품",
  },
  {
    image: "https://via.placeholder.com/1200x400",
    title: "실시간 주식 정보",
    subtitle: "빠르고 정확한 시장 동향",
  },
  {
    image: "https://via.placeholder.com/1200x400",
    title: "암호화폐 시세",
    subtitle: "글로벌 암호화폐 동향",
  },
];

// 각 탭별 테이블 헤더 정의
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

const getHeaders = computed(() => headers[currentTab.value]);

const getItems = computed(() => items[currentTab.value]);
</script>

<style scoped>

</style>
