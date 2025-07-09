<template>
    <n-card>
        <n-tabs class="card-tabs" default-value="signin" size="large" animated pane-wrapper-style="margin: 0 -4px"
            pane-style="padding-left: 4px; padding-right: 4px; box-sizing: border-box;">
            <n-tab-pane name="signin" tab="登录">
                <n-form>
                    <n-form-item-row label="用户名">
                        <n-input v-model:value="loginForm.username" placeholder="请输入用户名" />
                    </n-form-item-row>
                    <n-form-item-row label="密码">
                        <n-input v-model:value="loginForm.password" type="password" show-password-on="click"
                            placeholder="请输入密码" />
                    </n-form-item-row>
                </n-form>
                <n-button type="primary" block secondary strong @click="handleLogin">
                    登录
                </n-button>
            </n-tab-pane>
            <n-tab-pane name="signup" tab="注册">
                <n-form>
                    <n-form-item-row label="用户名">
                        <n-input v-model:value="registerForm.username" placeholder="请输入用户名" />
                    </n-form-item-row>
                    <n-form-item-row label="邮箱">
                        <n-input v-model:value="registerForm.email" placeholder="请输入邮箱" />
                    </n-form-item-row>
                    <n-form-item-row label="密码">
                        <n-input v-model:value="registerForm.password" type="password" show-password-on="click"
                            placeholder="请输入密码" />
                    </n-form-item-row>
                    <n-form-item-row label="重复密码">
                        <n-input v-model:value="registerForm.confirmPassword" type="password" show-password-on="click"
                            placeholder="请再次输入密码" />
                    </n-form-item-row>
                </n-form>
                <n-button type="primary" block secondary strong @click="handleRegister">
                    注册
                </n-button>
            </n-tab-pane>
        </n-tabs>
    </n-card>
</template>

<script setup>
import { ref, reactive } from 'vue';
import { useMessage } from 'naive-ui'; // 引入 Naive UI 的消息提示

const message = useMessage(); // 初始化消息提示

// 登录表单数据
const loginForm = reactive({
    username: '',
    password: ''
});

// 注册表单数据
const registerForm = reactive({
    username: '',
    email:'',
    password: '',
    confirmPassword: ''
});

// 处理登录
const handleLogin = async () => {
    // 简单的客户端验证
    if (!loginForm.username || !loginForm.password) {
        message.warning('请输入用户名和密码！');
        return;
    }

    try {
        // 实际应用中，您应该将这里的 URL 替换为您的后端登录 API 地址
        const response = await fetch('/api/login', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(loginForm)
        });

        const data = await response.json();

        if (response.ok) {
            message.success(data.message || '登录成功！');
            // 登录成功后的逻辑，例如：
            // - 保存 token 到 localStorage/sessionStorage
            // - 跳转到其他页面
            console.log('登录成功数据:', data);
        } else {
            // 服务器返回错误
            message.error(data.message || '登录失败！');
            console.error('登录失败错误:', data);
        }
    } catch (error) {
        // 网络或其他请求错误
        message.error('网络请求失败，请稍后再试！');
        console.error('登录请求错误:', error);
    }
};

// 处理注册
const handleRegister = async () => {
    // 简单的客户端验证
    if (!registerForm.username || !registerForm.password || !registerForm.confirmPassword) {
        message.warning('请填写所有注册信息！');
        return;
    }
    if (registerForm.password !== registerForm.confirmPassword) {
        message.error('两次输入的密码不一致！');
        return;
    }

    try {
        // 实际应用中，您应该将这里的 URL 替换为您的后端注册 API 地址
        const response = await fetch('/api/register', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                username: registerForm.username,
                password: registerForm.password // 实际应用中，密码通常会加密处理后发送
            })
        });

        const data = await response.json();

        if (response.ok) {
            message.success(data.message || '注册成功！');
            // 注册成功后的逻辑，例如：
            // - 自动跳转到登录页
            // - 清空注册表单
            console.log('注册成功数据:', data);
            // 可以选择清空表单
            registerForm.username = '';
            registerForm.password = '';
            registerForm.confirmPassword = '';
        } else {
            // 服务器返回错误
            message.error(data.message || '注册失败！');
            console.error('注册失败错误:', data);
        }
    } catch (error) {
        // 网络或其他请求错误
        message.error('网络请求失败，请稍后再试！');
        console.error('注册请求错误:', error);
    }
};
</script>

<style scoped>
.card-tabs .n-tabs-nav--bar-type {
    padding-left: 4px;
}
</style>