const BASE_URL = "http://127.0.0.1:8000"
export async function getRooms() {
    const response = await fetch(`${BASE_URL}/api/v1/rooms/`);

    const json = await response.json();

    return json;
}