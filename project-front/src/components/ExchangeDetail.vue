<template>
  <v-dialog v-model="internalShow" persistent max-width="500px">
    <v-card>
      <v-btn icon @click="close">
        <v-icon>mdi-close</v-icon>
      </v-btn>
      <v-card-title>
        <v-spacer></v-spacer>
        <v-img :src="`/flag/${exchange.cur_unit}.png`" alt="국기" width="150" max-height="100" />
        <span class="text-h5 font-weight-bold ml-4">{{ exchange?.cur_nm || "정보 없음" }} ({{ exchange?.cur_unit || "" }})</span>
      </v-card-title>

      <v-divider></v-divider>

      <v-card-text>
        <v-row>
          <v-col cols="6">
            <div>
              매매기준율:
              <strong>{{ exchange?.deal_bas_r || "N/A" }}</strong>
            </div>
          </v-col>
        </v-row>

        <v-divider class="my-4"></v-divider>

        <v-row>
          <v-col cols="6">
            <div>사실 때: {{ exchange?.tts || "N/A" }}</div>
          </v-col>
          <v-col cols="6">
            <div>파실 때: {{ exchange?.ttb || "N/A" }}</div>
          </v-col>
        </v-row>
      </v-card-text>

      <v-divider></v-divider>

      <!-- 계산 버튼 -->
      <v-card-actions>
        <v-btn color="primary" block @click="openCalculator">
          <v-icon left>mdi-calculator</v-icon>
          환율 계산기
        </v-btn>
      </v-card-actions>
    </v-card>

    <!-- 환율 계산기 모달 -->
    <ExchangeCalculator v-model:show="isCalculatorModalOpen" :exchange="exchange" />
  </v-dialog>
</template>

<script setup>
import { ref, watch } from "vue";
import ExchangeCalculator from "@/components/ExchangeCalculator.vue";

const props = defineProps({
  exchange: Object,
  show: Boolean,
});

const emit = defineEmits(["update:show"]);

const internalShow = ref(props.show);
const isCalculatorModalOpen = ref(false);

watch(
  () => props.show,
  (newVal) => {
    internalShow.value = newVal;
  }
);

const close = () => {
  emit("update:show", false);
};

const openCalculator = () => {
  isCalculatorModalOpen.value = true;
};
</script>

<style scoped>
.text-success {
  color: green;
}
.text-danger {
  color: red;
}
.v-card-title {
  display: flex;
  align-items: center;
  flex-direction: column;
}
</style>
