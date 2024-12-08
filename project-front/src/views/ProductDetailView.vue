<template>
  <v-main class="product-detail" style="margin-top: 64px">
    <!-- 상품 제목 섹션 (이전과 동일) -->
    <v-card class="mb-8 rounded-xl" elevation="3">
      <v-card-title class="d-flex align-center pa-6">
        <v-img :src="`/bank_images/${product.kor_co_nm}.jpg`" max-width="120px" class="mr-6 rounded-lg" cover alt="상품 이미지"></v-img>
        <div class="flex-grow-1">
          <div class="text-h4 font-weight-bold mb-2">{{ product.fin_prdt_nm }}</div>
          <div class="text-subtitle-1 text-grey-darken-1">{{ product.kor_co_nm }}</div>
          <v-btn icon="mdi-chart-bar" v-if="!isExpanded" @click="toggleDetails"></v-btn>
          <v-btn icon="mdi-chart-bar" v-if="isExpanded" @click="toggleDetails"></v-btn>
        </div>
        <v-btn v-if="isLogin" class="ml-4" :color="isLiked ? 'red' : 'grey'" icon="mdi-heart" variant="flat" size="large" @click="toggleLike" :elevation="isLiked ? 2 : 0"></v-btn>
      </v-card-title>
    </v-card>
    <v-expand-transition>
      <div v-show="isExpanded">
        <ProductWithOptions :productId="product.id" />
      </div>
    </v-expand-transition>
    <!-- 상품 정보 섹션 (수정된 부분) -->
    <v-row class="mb-8">
      <v-col cols="12">
        <v-card elevation="2" class="rounded-xl">
          <v-card-title class="text-h5 font-weight-bold pa-6">
            <v-icon color="primary" class="mr-2">mdi-information-outline</v-icon>
            상품 정보
          </v-card-title>

          <v-card-text class="pa-4">
            <v-row>
              <v-col v-for="(item, index) in productDetails" :key="index" cols="12" sm="6" lg="4">
                <v-card variant="outlined" class="pa-4 h-100">
                  <div class="d-flex align-center mb-2">
                    <v-icon :color="'primary'" size="24" class="mr-2">mdi-{{ getIcon(item.label) }}</v-icon>
                    <span class="text-h6 font-weight-medium">{{ item.label }}</span>
                  </div>
                  <div class="text-body-1 text-grey-darken-1 ml-9">
                    {{ item.value || "정보 없음" }}
                  </div>
                </v-card>
              </v-col>
            </v-row>
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>

    <!-- 상품 설명 -->
    <v-card class="mb-8 rounded-xl" elevation="2">
      <v-card-title class="text-h5 font-weight-bold pa-6">
        <v-icon color="primary" class="mr-2">mdi-text-box</v-icon>
        상품 설명
      </v-card-title>
      <v-card-text class="pa-6 text-body-1">
        {{ product.etc_note || "상품 설명이 없습니다." }}
      </v-card-text>
    </v-card>

    <!-- 지도 섹션 -->
    <v-card class="mb-8 rounded-xl overflow-hidden" elevation="2">
      <v-card-title class="text-h5 font-weight-bold pa-6">
        <v-icon color="primary" class="mr-2">mdi-map-marker</v-icon>
        지점 위치
      </v-card-title>
      <BankMap :bank="product.kor_co_nm" @error="handleError" />
    </v-card>

    <!-- 댓글 섹션 -->
    <ProductComments :productId="product.id" />
    <!-- 상품 더 상세 정보 보기-->
  </v-main>
</template>

<script setup>
import BankMap from "@/components/BankMap.vue";
import { useAccount } from "@/stores/accounts";
import { useFinStore } from "@/stores/financial";
import ProductComments from "@/components/ProductComments.vue";
import axios from "axios";
import { computed, onMounted, ref, watch } from "vue";
import ProductWithOptions from "@/components/ProductWithOptions.vue";

const store = useFinStore();
const product = computed(() => store.selectedProduct);

const accountStore = useAccount();
const isLogin = computed(() => accountStore.isLogin);
const isClicked = ref(false);
const isLiked = ref(false);
const isExpanded = ref(false);
const handleOpenDialog = () => {
  isClicked.value = true;
};

// 다이얼로그 상태 업데이트
const handleDialogState = (newVal) => {
  isClicked.value = newVal;
};
const toggleDetails = () => {
  isExpanded.value = !isExpanded.value;
};

const chartData = {
  labels: ["1개월", "3개월", "6개월", "12개월", "24개월", "36개월"],
  baseRates: [2.5, 2.8, 3.0, 3.2, 3.1, 3.0],
  maxRates: [3.0, 3.3, 3.5, 3.6, 3.4, 3.3],
};

const getIcon = (label) => {
  const icons = {
    // "상품 코드": "barcode",
    // "금융사 코드": "bank",
    "가입 대상": "account-group",
    "가입 방법": "card-account-details",
    "특별 조건": "star-circle",
  };
  return icons[label] || "information";
};

const productDetails = [
  // { label: "상품 코드", value: product.value.fin_prdt_cd },
  // { label: "금융사 코드", value: product.value.fin_co_no },
  { label: "가입 대상", value: product.value.join_member },
  { label: "가입 방법", value: product.value.join_way },
  { label: "특별 조건", value: product.value.spcl_cnd },
];

const toggleLike = async () => {
  if (!isLogin) {
    accountStore.showLoginMoal = true;
    return;
  }
  try {
    const token = accountStore.token;
    const headers = {
      Authorization: `Token ${token}`,
    };
    if (isLiked.value) {
      await axios.delete(`${store.API_URL}/api/financials/products/${product.value.id}/like/`, { headers });
      isLiked.value = false;
    } else {
      await axios.post(`${store.API_URL}/api/financials/products/${product.value.id}/like/`, {}, { headers });
      isLiked.value = true;
    }
  } catch (error) {
    swal({
      title: "실패",
      text: "좋아요 중 문제가 발생했습니다. 다시 시도해주세요.",
      icon: "error",
      button: "확인",
    });
  }
};

onMounted(async () => {
  try {
    const token = accountStore.token;
    const headers = {
      Authorization: `Token ${token}`,
    };
    const response = await axios.get(`${store.API_URL}/api/financials/products/${product.value.id}/like/`, { headers });
    isLiked.value = response.data.is_liked;
  } catch (error) {
    console.error(error);
    // swal({
    //   title: "실패",
    //   text: "데이터 로드 중 문제가 발생했습니다. 다시 시도해주세요.",
    //   icon: "error",
    //   button: "확인",
    // });
  }
});
</script>

<style scoped>
.product-detail > * {
  margin: 10px;
}
.v-card {
  transition: transform 0.2s, box-shadow 0.2s;
}

.v-card:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1) !important;
}

.v-textarea :deep(.v-field__input) {
  padding: 16px;
}

/* 상품 정보 카드 스타일 */
.v-card.v-card--variant-outlined {
  border: 1px solid rgba(var(--v-theme-primary), 0.12);
  transition: border-color 0.2s;
}

.v-card.v-card--variant-outlined:hover {
  border-color: rgba(var(--v-theme-primary), 0.5);
}
</style>
