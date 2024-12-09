import {Outlet} from "react-router";

export default function Root() {
    return <h1>
        im root<Outlet/>
    </h1>
}