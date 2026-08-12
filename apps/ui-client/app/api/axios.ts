// import axios from "axios";
// import type { AxiosRequestConfig } from "axios";

// export const api = async <T>(config: AxiosRequestConfig): Promise<T> => {
//   const instance = axios.create({
//     baseURL: "http://0.0.0.0:8000/",
//     withCredentials: true,
//   });

//   const response = await instance(config);
//   return response.data;
import axios from "axios";
import type { AxiosRequestConfig } from "axios";
export const api = async <T>(
  url: string,
  config?: AxiosRequestConfig,
): Promise<T> => {
  // console.log(`import da ui aqui: ${import.meta.env.AUTOMATION_HUB}`);
  const instance = axios.create({
    baseURL: import.meta.env.AUTOMATION_HUB,
    withCredentials: true,
  });

  const response = await instance(url, config);

  return {
    data: response.data,
    status: response.status,
    headers: new Headers(response.headers as HeadersInit),
  } as T;
};
