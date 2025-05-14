// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import { getAnalytics } from "firebase/analytics";
import { getAuth } from "firebase/auth";
import { getFirestore } from "firebase/firestore";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: "AIzaSyCtubdq8wj5hWohIkuV6pSf2VQe1D9lZIQ",
  authDomain: "aulasm2025-b892f.firebaseapp.com",
  projectId: "aulasm2025-b892f",
  storageBucket: "aulasm2025-b892f.firebasestorage.app",
  messagingSenderId: "618683157576",
  appId: "1:618683157576:web:1e28c8b0375beaf24cdc7d",
  measurementId: "G-0QP7KLBW2R",
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
export const auth = getAuth(app);
export const db = getFirestore(app);
const analytics = getAnalytics(app);
