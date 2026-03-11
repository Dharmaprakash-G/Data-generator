import { useState } from "react"

import Container from "../components/layout/Container"
import GenerateButton from "../components/generator/GenerateButton"
import PreviewPanel from "../components/generator/PreviewPanel"
import TableBuilder from "../components/generator/TableBuilder"
import { generateData } from "../services/api"
import type { Table } from "../types/generator"


function GeneratePage() {

    const [tables, setTables] = useState<Table[]>([
        {
            id: crypto.randomUUID(),
            table_name: "",
            rows: 10,
            columns: [],
        },
    ]);
    const [loading, setLoading] = useState(false);

    const handleGenerate = async () => {
        try {
            setLoading(true);

            const payload = { tables };

            const blob = await generateData(payload as any);

            const url = window.URL.createObjectURL(blob);
            const link = document.createElement("a");
            link.href = url;
            link.download = "generated_data.zip";
            link.click();

            window.URL.revokeObjectURL(url);
        } catch (error) {
            console.error(error);
            alert("Error generating data");
        } finally {
            setLoading(false);
        }
    };

    return (
        <Container>
            <h1 className="text-3xl font-bold mb-2 text-gray-800">
                GeneratorX
            </h1>
            <p className="text-gray-500 mb-8">
                Generate relational test data instantly.
            </p>

            <div className="grid grid-cols-1 lg:grid-cols-2 gap-8">
                <div className="max-h-[75vh] overflow-y-auto pr-2">
                    <TableBuilder tables={tables} setTables={setTables} />
                    <GenerateButton
                        onClick={handleGenerate}
                        loading={loading}
                        disabled={tables.length === 0}
                    />
                </div>

                <div className="max-h-[75vh] overflow-y-auto pr-2">
                    <h2 className="text-xl font-semibold mb-4">
                        Preview
                    </h2>
                    <PreviewPanel data={{ tables }} />
                </div>
            </div>



        </Container>
    )
}

export default GeneratePage