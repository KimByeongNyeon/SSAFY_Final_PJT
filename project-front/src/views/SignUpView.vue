<template>
  <v-container class="fill-height">
    <v-row align="center" justify="center">
      <v-col cols="12" sm="8" md="6">
        <v-card class="elevation-2 px-6 py-8">
          <v-card-title class="text-h5 font-weight-regular justify-center">회원가입</v-card-title>

          <v-form @submit.prevent="handleSubmit" v-model="isValid">
            <v-text-field v-model="email" label="이메일" :rules="emailRules" required prepend-inner-icon="mdi-email" variant="outlined" class="mb-2"></v-text-field>

            <v-text-field
              v-model="password"
              label="비밀번호"
              :rules="passwordRules"
              required
              :type="showPassword ? 'text' : 'password'"
              prepend-inner-icon="mdi-lock"
              :append-inner-icon="showPassword ? 'mdi-eye' : 'mdi-eye-off'"
              @click:append-inner="showPassword = !showPassword"
              variant="outlined"
              class="mb-2"
            ></v-text-field>

            <v-text-field
              v-model="passwordConfirm"
              label="비밀번호 확인"
              :rules="passwordConfirmRules"
              required
              :type="showPassword ? 'text' : 'password'"
              prepend-inner-icon="mdi-lock-check"
              variant="outlined"
              class="mb-2"
            ></v-text-field>

            <v-text-field v-model="name" label="이름" :rules="nameRules" required prepend-inner-icon="mdi-account" variant="outlined" class="mb-4"></v-text-field>

            <v-btn color="primary" block size="large" type="submit" :disabled="!isValid" class="mb-2">가입하기</v-btn>

            <v-btn color="secondary" block size="large" variant="text" to="/login">이미 계정이 있으신가요? 로그인하기</v-btn>
          </v-form>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
  data: () => ({
    isValid: false,
    email: "",
    password: "",
    passwordConfirm: "",
    name: "",
    showPassword: false,
    emailRules: [(v) => !!v || "이메일을 입력해주세요", (v) => /.+@.+\..+/.test(v) || "올바른 이메일 형식이 아닙니다"],
    passwordRules: [
      (v) => !!v || "비밀번호를 입력해주세요",
      (v) => v.length >= 8 || "비밀번호는 최소 8자 이상이어야 합니다",
      (v) => (/[A-Z]/.test(v) && /[a-z]/.test(v) && /[0-9]/.test(v)) || "대문자, 소문자, 숫자를 모두 포함해야 합니다",
    ],
    passwordConfirmRules: [(v) => !!v || "비밀번호를 한번 더 입력해주세요", (v) => v === this.password || "비밀번호가 일치하지 않습니다"],
    nameRules: [(v) => !!v || "이름을 입력해주세요", (v) => v.length >= 2 || "이름은 최소 2자 이상이어야 합니다"],
  }),

  methods: {
    handleSubmit() {
      if (this.isValid) {
        // API 호출 또는 회원가입 로직 구현
        console.log("Form submitted:", {
          email: this.email,
          password: this.password,
          name: this.name,
        });
      }
    },
  },
};
</script>
