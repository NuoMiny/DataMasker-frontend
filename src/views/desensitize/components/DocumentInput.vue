<template>
  <div class="text-box">
    <h4>输入待处理文本（txt格式）</h4>
    <el-input
      type="textarea"
      :rows="15"
      placeholder="请粘贴需要脱敏的文本内容"
      v-model="internalValue"
      resize="none"
      class="input-area"
    />
  </div>
</template>

<script>
import { ref, watch } from 'vue';

export default {
  props: {
    modelValue: {
      type: String,
      required: true
    }
  },
  setup(props, { emit }) {
    const internalValue = ref(props.modelValue);

    watch(internalValue, (newValue) => {
      emit('update:modelValue', newValue);
    });

    return {
      internalValue
    };
  }
};
</script>

<style scoped>
.input-area :deep(.el-textarea__inner) {
  font-family: Monaco, Consolas, monospace;
  line-height: 1.5;
}
</style>