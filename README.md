# Medicare-Formulary-Lookup

A streamlined web application designed to help pharmacists quickly look up Medicare plan IDs and navigate directly to third-party administrator websites, eliminating the need to search Medicare.gov first.

# Purpose

Pharmacists often need to verify insurance coverage and process claims through various third-party administrator websites. This tool provides instant access to the correct websites based on Medicare plan IDs, saving valuable time during patient interactions.

# Features

- **Quick Search**: Type any Medicare plan ID, plan name, or insurance company to find results instantly
- **Direct Links**: One-click access to third-party administrator websites
- **Comprehensive Database**: Pre-loaded with 22+ Medicare plans available in Wyoming
- **Easy Updates**: Add new plans as you encounter them
- **Search Statistics**: Track usage and database growth
- **Mobile Friendly**: Works on tablets and phones for pharmacy counter use
- **No Backend Required**: Runs entirely in the browser using local storage

## Getting Started

### Quick Start
1. Download the `medicare-database.html` file
2. Open it in any web browser
3. Start searching for plan IDs immediately

### For Development
```bash
# Clone the repository
git clone https://github.com/yourusername/medicare-plan-database.git

# Navigate to project directory
cd medicare-plan-database

# Open in browser
open medicare-database.html
```

## Pre-loaded Data

The database comes with plans from major Medicare providers in Wyoming:

### Medicare Advantage Plans (14 plans)
- **UnitedHealthcare/AARP**: H2001-044, H0019-003
- **Humana**: H1036-175, H5216-256
- **Aetna**: H5521-289, H0290-007
- **Cigna**: H3014-002
- **WellCare/Anthem**: H4922-005
- **Lasso Healthcare** (Wyoming-specific): H7207-001, H7207-002
- **Kaiser Permanente**: H0630-022
- **Anthem BCBS**: H0239-003
- **PFFS Plans**: H8768-001, H1304-012

### Part D Prescription Plans (8 plans)
- **AARP/UnitedHealthcare**: S5921-036, S5820-077
- **Humana**: S5884-114, S5617-042
- **SilverScript/Aetna**: S7692-048, S7692-102
- **Cigna**: S8722-103
- **WellCare**: S8768-140

## Usage

### Searching for Plans
1. Type any part of a plan ID (e.g., "H2001" or "044")
2. Search by plan name (e.g., "AARP Medicare")
3. Search by insurance company (e.g., "Humana")
4. Click the website link to navigate to the third-party site

### Adding New Plans
1. Scroll to the "Add New Plan" section
2. Fill in the required fields:
   - Plan ID (e.g., H1234-567)
   - Plan Name
   - Insurance Company
   - Third Party Website URL
   - Plan Type (dropdown)
   - Notes (optional)
3. Click "Add Plan"

### Plan ID Format
- Medicare Advantage plans: `H####-###` (e.g., H2001-044)
- Part D prescription plans: `S####-###` (e.g., S5921-036)
- Special Needs Plans: `H####-###` with SNP designation

## For Pharmacy Use

### Typical Workflow
1. Patient presents Medicare card
2. Enter plan ID in search box
3. Click link to access third-party website
4. Process prescription claim or verify coverage
5. Add new plans to database as encountered

### Best Practices
- Save the HTML file locally for offline access
- Update annually during Medicare open enrollment (Oct-Dec)
- Add notes for plans with special requirements
- Share updates with pharmacy team

## Technical Details

### Built With
- **Frontend**: Vanilla HTML, CSS, JavaScript
- **Storage**: Browser localStorage (no server required)
- **Styling**: Modern CSS with gradients and animations
- **Responsive**: Mobile-first design with Flexbox/Grid

### Browser Compatibility
- Chrome 60+
- Firefox 55+
- Safari 12+
- Edge 79+

### File Structure
```
medicare-plan-database/
├── medicare-database.html    # Main application file
├── README.md                # This file
├── LICENSE                  # MIT License
```
### Planned Features
- [ ] Export/Import database functionality
- [ ] Bulk plan upload from CSV
- [ ] Plan expiration date tracking
- [ ] Coverage area mapping
- [ ] Integration with pharmacy management systems
- [ ] Multi-state support beyond Wyoming

### Known Limitations
- Plan data stored in browser (cleared if browser data is cleared)
- Annual plan changes require manual updates
- No real-time plan validation with Medicare systems

## Contributing

We welcome contributions from pharmacists and developers!

### How to Contribute
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Contribution Guidelines
- Add new Medicare plans with accurate information
- Include source verification for plan data
- Test changes across different browsers
- Update documentation as needed

### Adding New Plans
When contributing new plans include:
- Verified plan ID from official sources
- Correct third-party administrator website
- Plan type and coverage areas
- Any special notes or requirements

## License

This project is licensed under the MIT License - see the License file for details.

### For Pharmacists
- Check the plan database annually for updates
- Report incorrect or outdated plan information
- Suggest new features that would improve workflow

### Technical Support
- Open an issue for bugs or feature requests
- Check existing issues before creating new ones
- Provide browser and operating system details for bug reports

## Statistics

- **22+ Pre-loaded Plans**: Covers major Wyoming Medicare providers
- **Instant Search**: Results appear as you type
- **Mobile Optimized**: Works on phones and tablets
- **Zero Dependencies**: No external libraries required

**Disclaimer**: This tool is for informational purposes only. Always verify plan details and coverage with official Medicare sources and third-party administrators. Plan availability and details may change annually during open enrollment periods.
