<template>
  <v-app-bar app flat color="#f8f9fa">
    <v-container>
      <v-row justify="space-between" align="center">
        <!-- 로고 영역 -->
        <v-col class="d-flex align-center">
          <v-icon>mdi-github</v-icon>
        </v-col>

        <!-- 메뉴 -->
        <v-col class="d-flex align-center" cols="auto">
          <v-btn text>금융상품</v-btn>
          <v-btn text>주식</v-btn>
          <v-btn text>비트코인</v-btn>
        </v-col>

        <!-- 로그인/회원가입 버튼 -->
        <v-col class="d-flex align-center" cols="auto">
          <v-btn outlined class="mr-2">Sign in</v-btn>
          <v-btn color="black" dark>Register</v-btn>
        </v-col>
      </v-row>
    </v-container>
  </v-app-bar>
</template>

<script setup>

</script>

<style scoped></style>
