import axios from "axios";
import {QueryFunctionContext, QueryKey} from "@tanstack/react-query";

const instance = axios.create({
    baseURL: "http://127.0.0.1:8000/api/v1/"
})
export const getRooms = () => instance.get(`rooms/`).then(response => response.data);

export const getRoom = (queryKey: QueryFunctionContext) => {
    const pk = queryKey.queryKey[1];
    return instance.get(`rooms/${pk}`).then(response => response.data)
};