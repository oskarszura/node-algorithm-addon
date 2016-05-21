{
    "targets": [
        {
            "target_name": "algorithms",
            "sources": [ "algorithms.cpp" ],
            "include_dirs": [
                "<!(node -e \"require('nan')\")"
            ]
        }
    ]
}
