interface Props {
    onClick?: () => void;
    loading?: boolean;
    disabled?: boolean;
}



function GenerateButton({ onClick, loading, disabled }: Props) {
    return (
        <div className="mt-6">
            <button
                className="w-full bg-blue-600 hover:bg-blue-700 text-white font-semibold py-3 rounded-lg transition duration-200"
                onClick={onClick}
                disabled={loading || disabled}
            >
                {loading ? "Generating..." : "Generate Data"}
            </button>
        </div>
    )
}

export default GenerateButton