import React, { useState } from "react";
import "../../styles/Dashboard.css";
import DashboardLeftSide from "./DashboardLeftSide";
import DashboardMainContent from "./DashboardMainContent";
import ProfileForm from "./ProfileForm"; // Crie este componente
import NursingMap from "./NursingMap";   // Crie este componente

const DashboardLayout = () => {
    const [activePage, setActivePage] = useState("dashboard");

    let content;
    if (activePage === "dashboard") {
        content = <DashboardMainContent />;
    } else if (activePage === "profile") {
        content = <ProfileForm />;
    } else if (activePage === "nursing") {
        content = <NursingMap />;
    }

    return (
        <div className="dashboard-container">
            <div className="dashboard-background">
                <DashboardLeftSide activePage={activePage} setActivePage={setActivePage} />
                {content}
            </div>
        </div>
    );
};

export default DashboardLayout;